import logging
import logging.handlers
import os.path
filedir = os.path.dirname(os.path.abspath(__file__))


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_filename=os.path.join(filedir,"logs/about.log")
th=logging.handlers.TimedRotatingFileHandler(log_filename,"D",1,10,encoding="utf-8")



formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s",datefmt="%Y-%m-%d %H:%M:%S")
th.setFormatter(formatter)

logger.addHandler(th)
logger.info("test")

