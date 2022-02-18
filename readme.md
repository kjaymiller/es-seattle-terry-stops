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
## [YOU ARE ON THE DOCKER COMPOSE BRANCH]
Instructions are setup for self-hosted reports. If you are looking for the Elastic Cloud instructions head to the [main branch](https://github.com/kjaymiller/es-seattle-terry-stops)

Set the environment variable `ES_CONNECTION_TYPE` to `local`
`ES_CONNECTION_TYPE=local`

## Index Name
Set the environment variable
`ES_INDEX="seattle-terry-stops` - name of the index to be created in Elasticsearch 

### Local/hosted Deployment
Connect to an hosted instance by setting the following environment. 

variables:
* `ES_VERSION=8.0.0` - elasticsearch version
* `ES_HOST="HTTPS://EXAMPLEHOST.COM:9200` - the address of your Elastic instance (defaults to localhost)
* `ES_PWD=changeme` - the password to connect to your Elasticsearch cluster (defaults to 'changeme') 
* `ES_USER=elastic` - the username of the account (defaults to 'elastic')


## Updating Dataset information
### Mappings - `mappings.json`
mappings for elasticsearch index. Only usable with `elasticsearch-py`. If no mappings, assume all fields are in text format.

### Socrata Connection Information - `socrata.json`
domain and dataset ids for socrata data
