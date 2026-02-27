import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError
from shapely.wkt import loads # We need shapely to deal with polygon data. Make sure you have Shapely installed by doing `pip install Shapely`

LOGGER = logging.getLogger(__name__)
PROCESS_METADATA = {
    'version': '0.2.0',
    'id': 'geom-details',
    'name' : 'geom-details',
    'title': {
        'en': 'Geometry Details',
    },
    'description': {
        'en': 'An example process that takes a WKT Polygon geometry as input and return information such as Area, Bounds, center'
    },
    'keywords': ['polygon', 'geometry'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://shapely.readthedocs.io/en/stable/reference/shapely.Polygon.html',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'polyWKT': {
            'title': 'Polygon',
            'description': 'WKT of Polygon',
            'schema': {
                'type': 'string'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': ['Polygon']
        }
    },
    'outputs': {
        'echo': {
            'title': 'Get Polygon Information',
            'description': 'Polygon WKT is returned',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'
            }
        }
    },
    'example': {
        "inputs": {
            "polyWKT": "POLYGON ((73.65865031385647 17.77623164372008, 73.65897114729012 17.777001795974, 73.65825595609473 17.776963606683765, 73.65817351972652 17.776647483916918, 73.65852108927962 17.7764247125032, 73.65865031385647 17.77623164372008))"
        }
}
}

class GeomProcessor(BaseProcessor):
    """Geom Processor example"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.geom_details.GeomProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):

        mimetype = 'application/json'
        polygon = data.get('polyWKT', None)
        if polygon is None:
            raise ProcessorExecuteError('Cannot process without a Polygon WKT')

        try :
            g = loads(polygon)
            value = {
                'area': g.area,
                'bounds' : g.bounds,
                'centroid': g.centroid.wkt
            }
        except:
            value = 'Error in polygon WKT, please try again'

        outputs = {
            'result': value
        }

        return mimetype, outputs

    def __repr__(self):
        return '<GeomProcessor> {}'.format(self.name)
