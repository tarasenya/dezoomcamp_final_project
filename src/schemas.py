from google.cloud.bigquery import SqlTypeNames
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime, date
from pyspark.sql import types
class KoalaScheme(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    objectid: int
    globalid: str
    sighttime: datetime
    sightdate: date
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

spark_schema = types.StructType([
    types.StructField('objectid', types.LongType(), False),
    types.StructField('globalid', types.StringType(), False),
    types.StructField('sighttime', types.TimestampType(), False),
    types.StructField('sightdate', types.DateType(), False),
    types.StructField('joeypresent',types.StringType(), True),
    types.StructField('numberofkoala', types.LongType(), True),
    types.StructField('koalacondifinal', types.StringType(), True),
    types.StructField('locality',types.StringType(), True ),
    types.StructField('near_koala_habitat', types.StringType(), True),
    types.StructField('attachment_cc_lic_check', types.StringType(), True),
    types.StructField('lga',types.StringType(), True),
    types.StructField('sighting_lat_wgs84', types.DoubleType(), True),
    types.StructField('sighting_long_wgs84', types.DoubleType(), True),
    types.StructField('vetting_code', types.StringType(), True),
    types.StructField('gis_x', types.DoubleType(), False),
    types.StructField('gis_y', types.DoubleType(), False)
])

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