# Seattle Terry Stop Data Visualizations via Elasticsearch
Index the Seattle Terry Stops data from the City of Seattle.

Find more about this data at [Seattle's Open Data Portal](https://data.seattle.gov/Public-Safety/Terry-Stops/28ny-9ts8)

## Disclosure
This repo is for educational purposes and should not be used for identification purposes.

## How to Use this Repo
- Setup Elasticsearch Cluster
- Fork Repo
- setup python environment
- run `ingest.py`

## How this repo works.
This dataset loads the data via [Socrata](https://dev.socrata.com) and ingests it into elasticsearch.

Mappings are translated based on the columns provided.
Any mutations will be annotated in [data_change_notes.md](./data_change_notes.md)

## Requirements
- Python 3.7+
- Elasticsearch Version 7.0+
- modules in requirements including (but not limited to):
  - [sodapy](https://pypi.org/project/sodapy/)
  - [elasticsearch](https://elasticsearch-py.readthedocs.io/)
  
## Connect to Elasticsearch
Set the environment variable `ES_CONNECTION_TYPE` to `cloud`
* `ES_CONNECTION_TYPE=cloud` - Elastic Cloud

## Index Name
Set the environment variable
* `ES_INDEX=es-terry-stops` - name of the index to be created in Elasticsearch 

### Elastic Cloud
Connect to an Elastic Cloud instance by setting the following environment
variables:

* `ES_CLOUD_ID=<MYCLOUDID1234567890>` - the cloud_id of your Elastic instance 
* `ES_PWD=<CLOUDPWD>` - the password to connect to your Elasticsearch cluster 
* `ES_USER=elastic` - the username of the account (defaults to 'elastic') 

Neither ES_CLOUD_ID nor ES_PWD have defaults. You will not be able to connect without setting them or modifying `connection.py`
For help setting up Elastic Cloud check [this discussion post](https://github.com/kjaymiller/es-seattle-terry-stops/discussions/7) and visit <https://cloud.elastic.co>.
### Local/hosted Deployment
Instructions for self-hosted docker compose setup on the [docker-compose branch](https://github.com/kjaymiller/es-seattle-terry-stops/tree/docker-compose)
## Updating Dataset information
### Mappings - `mappings.json`
mappings for elasticsearch index. Only usable with `elasticsearch-py`. If no mappings, assume all fields are in text format.

### Socrata Connection Information - `socrata.json`
domain and dataset ids for socrata data