import os
import json
from typing import Optional, Sequence

import sodapy
from elasticsearch.helpers import parallel_bulk

from connection import get_es_connection

with open("socrata.json") as f:
    soda_info = json.load(f)


def bulk_mapper(soda_client: Sequence) -> dict[str:str]:
    """ Map Socrata dataset to a bulk indexable format.

    :param soda_client: Socrata client
    :return: dict of bulk indexable format

    Use .get() for testing mapping and data changes
    ```
    soda_data = soda_client.get(
                soda_info["dataset_id"],
                limit=10,
                order="terry_stop_id DESC",
        ) 
    ```
    """
    
    soda_data = soda_client.get_all(soda_info["dataset_id"])

    for row in soda_data:
        data = {x: y for x, y in row.items()}
        new_row = {}

        for key, val in data.items():
            if val == "-1":
                continue

            val = val.lstrip("-")

            if val.lower() not in ["", "-", "none"] or key == "weapon_type":
                # we want to include None values for Weapon Type
                new_row[key] = val

            if key in ["friskflag", "arrestflag"]: # boolean values
                new_row[key] = val.lower() in ["y", "true", "yes", "1"]

        yield new_row


def load(index: str, / ) -> None:
    """ Load Socrata data into Elasticsearch.
    
    :param index: Elasticsearch index name
    :return: None
    """

    soda_client = sodapy.Socrata(
        soda_info["domain"],
        os.environ.get("SOCRATA_APP_TOKEN", None),
        timeout=45,
    )

    with open("mappings.json") as f:
        mappings = json.load(f)

    client = get_es_connection(os.environ.get("ES_CONNECTION_TYPE", "local"))
    client.indices.delete(
        index=index, ignore_unavailable=True
    )  # delete index if it exists
    client.indices.create(index=index, mappings=mappings)

    for ok, result in parallel_bulk(
        client, bulk_mapper(soda_client), index=index, thread_count=10
    ):
        pass


if __name__ == "__main__":
    load(index=os.environ.get('ES_INDEX', 'test_index'))
