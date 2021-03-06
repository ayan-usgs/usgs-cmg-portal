import logging
import logging.handlers

from sciwms_connect import SCIWMS_REST_URL, USER, PASSWORD
from sciwms_iso import add_dataset_to_sciwms, get_metadata


logger_name = 'thredds_crawler'
logger = logging.getLogger('thredds_crawler')
fh = logging.handlers.RotatingFileHandler('/usgs/data0/iso/logs/iso_harvest.log', maxBytes=1024*1024*10, backupCount=5)
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)

SAVE_DIR="/usgs/data0/iso/iso_records"

THREDDS_SERVERS = {
   "usgs-ts":   "http://geoport.whoi.edu/thredds/catalog/usgs/data2/emontgomery/stellwagen/CF-1.6/catalog.html"
}

metadata_files = get_metadata(thredds_servers=THREDDS_SERVERS,
                              save_dir=SAVE_DIR,
                              logger_name=logger_name
                              )
add_dataset_to_sciwms(rest_url=SCIWMS_REST_URL,
                      user=USER,
                      password=PASSWORD,
                      metadata_files=metadata_files,
                      logger_name=logger_name
                      )
