# Seattle Terry Stop Data Visualizations via Elasticsearch
Index the Seattle Terry Stops data from the City of Seattle.

Find more about this data at [Seattle's Open Data Portal](https://data.seattle.gov/Public-Safety/Terry-Stops/28ny-9ts8)

## How this repo works.
This dataset loads the data via [Socrata](https://dev.socrata.com) and ingests it into elasticsearch.

Mappings are translated based on the columns provided. Any mutations will be annotated with
reasoning below.

### Modified
---
No Modifications at this time

### Removed
---
No Removals at this time


**[Note]** other mappings may be defined in Elasticsearch based on this information and not listed in this repository.

## Requirements
- Python 3.10+
- modules in requirements including (but not limited to):
  - [sodapy](https://pypi.org/project/sodapy/)
  - [elasticsearch](https://elasticsearch-py.readthedocs.io/)
  

