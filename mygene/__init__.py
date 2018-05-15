'''
Python Client for MyGene.Info services
'''
from biothings_client import get_client

__version__ = '3.0.0'

class MyGeneInfo(get_client('gene', instance=False)):
    pass
