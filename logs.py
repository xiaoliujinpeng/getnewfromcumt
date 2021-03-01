import logging
import logging.handlers
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


th=logging.handlers.TimedRotatingFileHandler("logs/about.log","D",1,10,encoding="utf-8")



formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s",datefmt="%Y-%m-%d %H:%M:%S")
th.setFormatter(formatter)

logger.addHandler(th)
logger.info("test")

