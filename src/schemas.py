from google.cloud.bigquery import SqlTypeNames
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class KoalaScheme(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    
    objectid: int
    globalid: str
    sighttime: datetime
    joeypresent: Optional[str] = None
    numberofkoala: Optional[int] = None
    koalacondifinal: Optional[str] = None
    locality: Optional[str] = None
    near_koala_habitat: Optional[str] = None
    attachment_cc_lic_check: Optional[str] = None
    lga: Optional[str] = None
    sighting_lat_wgs84: Optional[float] = None
    sighting_long_wgs84: Optional[float] = None
    vetting_code: Optional[str] = None
    gis_x: float
    gis_y: float


koala_schema = [{
    'name': 'objectid',
    'type': SqlTypeNames.INTEGER,
    'mode': 'REQUIRED'},
    {
    'name': 'globalid',
    'type': SqlTypeNames.STRING,
    'mode': 'REQUIRED'
    },
    {'name':'sighttime',
     'type': SqlTypeNames.TIMESTAMP,
     'mode': 'REQUIRED'},
     {
    'name':'joeypresent',
    'type': SqlTypeNames.STRING,
    'mode': 'NULLABLE',
     },
    {'name': 'numberofkoala',
     'type': SqlTypeNames.INTEGER,
     'mode': 'REQUIRED'
    },
    {'name':'koalacondifinal',
     'type':SqlTypeNames.STRING,
     'mode': 'NULLABLE',
    },
    {'name':'locality',
     'type': SqlTypeNames.STRING,
     'mode': 'NULLABLE'},

     {'name': 'near_koala_habitat',
      'type': SqlTypeNames.STRING,
      'mode': 'NULLABLE'},
    {'name':'attachment_cc_lic_check',
     'type': SqlTypeNames.STRING,
     'mode': 'NULLABLE'},
    {'name': 'lga',
     'type': SqlTypeNames.STRING,
     'mode': 'NULLABLE'
    },
    {'name': 'sighting_lat_wgs84',
     'type': SqlTypeNames.FLOAT, 
     'mode': 'NULLABLE'
    },
    {'name': 'sighting_long_wgs84',
     'type': SqlTypeNames.FLOAT,
     'mode': 'NULLABLE'}, 
    {'name':'vetting_code',
     'type': SqlTypeNames.STRING,
     'mode': 'NULLABLE'},
    {'name': 'gis_x',
     'type': SqlTypeNames.FLOAT,
     'mode': 'NULLABLE'},
    {'name':'gis_y',
     'type': SqlTypeNames.FLOAT,
     'mode': 'NULLABLE'}
]