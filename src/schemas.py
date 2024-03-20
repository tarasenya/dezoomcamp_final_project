from google.cloud.bigquery import SqlTypeNames

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