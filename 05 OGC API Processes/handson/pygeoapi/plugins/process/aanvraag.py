from os import makedirs, path
from logging import getLogger


from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

import geopandas as gpd
import numpy as np

PROCESS_METADATA = {
    'version': '0.1',
    'id': 'aanvraag',
    'title': 'Aanvraag kapvergunning',
    'description': 'Demo om persoonsgegeven en object samen te loggen',
    'keywords': ['aanvraag', 'kapvergunning', 'otel demo'],
    "jobControlOptions": [
				"sync-execute"
	],

    'inputs':{
        'dataset':{
            'title': 'Dataset',
            'description': 'geojson dataset of points, in one CRS. ',
            "schema": { "type": "string", "format": "url" },
            'minOccurs': 1,
            'maxOccurs': 1,
            'keywords': ['geojson ogc api features', 'point data']
        },
        'object_id':{
            'title': 'The object id for which a permit is requested',
            'description': 'The object id for which a permit is requested.',
            'minOccurs': 0,
            'maxOccurs': 1,
            'schema': {
                'oneOf': ['integer'],
                # 'defaultValue': 20,
            }
        }, 
        'subject_id':{
            'title': 'The subject id',
            'description': 'ID of the person requesting the permit',
            'minOccurs': 0,
            'maxOccurs': 1,
            'schema': {
                'oneOf': ['string'],
                # 'defaultValue': 30,
            },
        },
    },
    'outputs': {
        'output_dataset':{
            'title': 'Output Dataset',
            'description': 'output',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'
                }
            },
    },
    'example': {"inputs": 
    {
        "dataset": "http://localhost/collections/bomen/items?f=json&limit=1000", 
        "object_id": 2069296, 
        "subject_id": "Meneer van Eik"
    }
}
}

class AanvraagProcessor(BaseProcessor):
   

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.aanvraag.AanvraagProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)
    
    def execute(self, data):
       
            obj_id = int(data.get('object_id'))
            subj_name = data.get('subject_id', '')
            dataset = data.get("dataset")

            if dataset is None:
                raise ProcessorExecuteError('Cannot process without input dataset')
            
            gdf = gpd.read_file(dataset)

            
            gdf['kap_aanvraag'] = np.where(gdf['id'].astype(int) == obj_id, subj_name, '0')
            gdf_out = gdf[gdf['kap_aanvraag'] != '0']
            
            gdf_out = gdf_out[['id','leaf_type','geometry','species:nl','kap_aanvraag']]
            mimetype = 'application/geo+json'
            outputs = {
                        'id': 'output_dataset',
                        'value': gdf_out.to_json()
                    }

            return mimetype, outputs

    def __repr__(self):
        return '<AanvraagProcessor> {}'.format(self.name)