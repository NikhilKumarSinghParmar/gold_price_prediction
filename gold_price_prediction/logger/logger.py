import os
import sys
import logging
from datetime import datetime

months=[
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]


month_name=months[int(datetime.now().strftime("%m"))-1]

LOG_FILE=f"{month_name}{datetime.now().strftime("%d_%y__%Hh_%Mm_%Ss")}.log"
LOG_FILE_PATH=os.path.join(os.getcwd(),"logs",LOG_FILE)

dir_path=os.path.dirname(LOG_FILE_PATH)
os.makedirs(dir_path,exist_ok=True)


format = "[%(asctime)s] --%(filename)s-- (line number - %(lineno)d) -- %(levelname)s -> %(message)s"
dateformat="%d/%m/%y %H:%M:%S"

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format=format,
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
)



if __name__=="__main__":
    logging.info("logger file is created")
    logging.info("use like logger.info(..information..)")
