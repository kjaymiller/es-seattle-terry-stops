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

Mappings are translated based on the columns provided. Any mutations will be annotated with
reasoning below.

### Modified
---
No Modifications at this time

### Removed
---
No Removals at this time


### Notes
---
* Reported Date/Reported Time do not correlate to the date/time of the stop. For this
  reason, we will not use _Reported Time_ logging metrics. Reported Date is most often within
  1-day of incident. For this reason date based data will not be accurate for pinpointing a
  particular incident
  fields

**[Note]** other mappings may be defined in Elasticsearch based on this information and not listed in this repository.

## Requirements
- Python 3.6+ (though 3.7+ is supported)
- Elasticsearch Version 7.0+
- modules in requirements including (but not limited to):
  - [sodapy](https://pypi.org/project/sodapy/)
  - [elasticsearch](https://elasticsearch-py.readthedocs.io/)
  
## Connect to Elasticsearch
`connection.py` has two modules designed to read your environment variables. Import the
  connection that best fits your elasticsearch setup.

### Elastic Cloud
Connect to an Elastic Cloud instance by setting the following environment
variables:

* `ES_CONNECTION_TYPE=cloud` 
* `ES_CLOUD_ID` - the cloud_id of your Elastic instance 
* `ES_INDEX` - name of the index to be created in Elasticsearch 
* `ES_PWD` - the password to connect to your Elasticsearch cluster 
* `ES_USER` - the username of the account (defaults to 'elastic') 

Neither ES_CLOUD_ID nor ES_PWD have defaults. You will not be able to connect without setting them or modifying `connection.py`

### Local/hosted Deployment
Connect to an hosted instance by setting the following environment
variables:

* `ES_CONNECTION_TYPE=local` (default)
* `ES_HOST` - the address of your Elastic instance (defaults to localhost)
* `ES_INDEX` - name of the index to be created in Elasticsearch
* `ES_PWD` - the password to connect to your Elasticsearch cluster (defaults to 'elastic') 
* `ES_USER` - the username of the account (defaults to 'elastic')


## Updating Dataset information
Some information is provided via json files to make transfer/modification of information
easier.

### Mappings - `mappings.json`
mappings for elasticsearch index. Only usable with `elasticsearch-py`. If no mappings, assume all fields are in keyword format.

### Socrata Connection Information - `socrata.json`
domain and dataset ids for socrata data