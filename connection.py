from elasticsearch import Elasticsearch
import os

def get_es_connection(format:str) -> Elasticsearch:
    """
    Returns an Elasticsearch connection object.
    """
    if format == 'local':
        return Elasticsearch(
            hosts = [os.environ.get('ES_HOST', 'http://localhost:9200')],
            http_auth = (os.environ.get('ES_USER', 'elastic'), os.environ.get('ES_PWD', 'elastic')),
        )

    elif format == 'cloud':
        return Elasticsearch(
            cloud_id = os.environ.get('ES_CLOUD_ID', ''),
            http_auth = (os.environ.get('ES_USER', 'elastic'), os.environ.get('ES_PWD', None)),
        )

    else:
        raise ValueError(f'Invalid format: {format}. Must be one of local/cloud')
