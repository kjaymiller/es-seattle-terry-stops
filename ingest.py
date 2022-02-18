import os
import json
from typing import Optional, Sequence

import sodapy
from elasticsearch.helpers import bulk

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
        new_row = {}

        for key, val in row.items():
            
            # Check for not entered values and skip them
            if key == 'subject_id', and val == "-1":
                continue

            if val.lower() in ["", "-", "none"] and key != "weapon_type": 
                # skips unmarked values EXCEPT for weapon_type
                continue

            # frisk and arrest flages are boolean values
            if key in ["friskflag", "arrestflag"]:
                new_row[key] = val.lower() in ["y", "true", "yes", "1"]

            # most data
            else:
                val = val.lstrip("-").strip() # removes whitespace and -


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

    return bulk(client, bulk_mapper(soda_client), index=index, thread_count=10)


if __name__ == "__main__":
    load(index=os.environ.get('ES_INDEX', 'test_index'))
