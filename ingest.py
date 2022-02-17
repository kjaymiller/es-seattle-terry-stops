import os
import json
from typing import Optional, Sequence

from slugify import slugify
import sodapy
from elasticsearch.helpers import parallel_bulk

from connection import get_es_connection

with open("socrata.json") as f:
    soda_info = json.load(f)


def bulk_mapper(soda_client: Sequence) -> dict[str:str]:
    #    soda_data = soda_client.get(
    #            soda_info["dataset_id"],
    #            limit=10,
    #            order="terry_stop_id DESC",
    #    )  # loads partial data for testing

    soda_data = soda_client.get_all(
        soda_info["dataset_id"],
    )

    for row in soda_data:
        data = {slugify(x, separator="_"): y for x, y in row.items()}
        new_row = {}

        for key, val in data.items():
            if val == "-1":
                continue

            val = val.lstrip("-")

            if val.lower() not in ["", "-", "none"] or key == "weapon_type":
                # we want to include None values for Weapon Type
                new_row[key] = val

            if key in ["friskflag", "arrestflag"]:
                new_row[key] = val.lower() in ["y", "true", "yes", "1"]

        yield new_row


def load(index: Optional[str] = None) -> None:

    soda_client = sodapy.Socrata(
        soda_info["domain"],
        os.environ.get("SOCRATA_APP_TOKEN", None),
        timeout=45,
    )

    if not index:
        index = os.environ.get(
            "ES_INDEX", os.environ.get(soda_data.get(["soda_dataset_id"]))
        )

    with open("mappings.json") as f:
        mappings = json.load(f)

    client = get_es_connection("local")
    client.indices.delete(
        index=index, ignore_unavailable=True
    )  # delete index if it exists
    client.indices.create(index=index, mappings=mappings)

    for ok, result in parallel_bulk(
        client, bulk_mapper(soda_client), index=index, thread_count=10
    ):
        pass

if __name__ == "__main__":
    load(index="seattle-terry-stops")
