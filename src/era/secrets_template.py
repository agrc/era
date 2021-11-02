"""
secrets_template.py: Example secrets file. Copy to 'secrets.py' and populate with actual values.
DO NOT ADD new secrets.py to version control.
"""

import logging
import socket
from pathlib import Path

import numpy as np

#: AGOL Account Settings
AGOL_ORG = 'https://utah.maps.arcgis.com'
AGOL_USER = ''
AGOL_PASSWORD = ''

#: Settings for Supervisor's SendGridHandler
SENDGRID_SETTINGS = {
    'api_key': '',
    'from_address': 'noreply@utah.gov',
    'to_addresses': '',
    'prefix': f'ERA on {socket.gethostname()}: ',
}

#: Logging Settings
LOG_LEVEL = logging.INFO
ROTATE_COUNT = 90
ERAP_BASE_DIR = Path()
ERAP_LOG_PATH = ERAP_BASE_DIR / 'log.txt'

#: SFTP Settings
SFTP_HOST = ''
SFTP_USERNAME = ''
SFTP_PASSWORD = ''
SFTP_FOLDER = ''  #: Folder on SFTP host to download from, relative to users home dir
KNOWNHOSTS = f'{Path(__file__).parent.parent.parent}\\known_hosts'
ERAP_FILE_NAME = ''
ERAP_DATA_TYPES = {  #: Column names and types for csv -> dataframe conversion
    'zip5': str,
    'Count_': str,
    'Amount': np.float64,
    'Updated': str,
}

#: Feature Service Updating Settings
ERAP_KEY_COLUMN = ''  #: The column in the new dataframe that is the key between it and the feature service
ERAP_FEATURE_SERVICE_URL = ''  #: Should go directly to the layer in the feature service, ending in /0 (or /1, whatever)

#: Reclassification Settings
ERAP_WEBMAP_ITEMID = ''
ERAP_LAYER_NAME = ''
ERAP_CLASSIFICATION_COLUMN = ''  #: The new ranges will be calculated from this column in ERAP_LAYER_NAME's data
