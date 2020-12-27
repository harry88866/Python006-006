import logging
from pathlib import Path
from datetime import datetime

def log_func():
    dateStr = datetime.today().strftime('%Y-%m-%d')
    path = Path('/var/log/python-' + dateStr + '/')
    if not path.exists():
        path.mkdir()
    name = '/var/log/python-' + dateStr + '/app.log'
    logging.basicConfig(filename=name,level=logging.INFO)
    logging.info('call function')
log_func()
    
     