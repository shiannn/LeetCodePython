import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(thread)s - %(levelname)s : %(message)s',
                    filename='mylog.txt')
logging.critical("critical message")  
logging.debug("debug message")  
logging.info("info message")  
logging.warning("warning message")  
logging.error("error message")  
logging.critical("critical message\n")  
