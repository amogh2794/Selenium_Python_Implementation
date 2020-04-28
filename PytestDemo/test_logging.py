import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logsfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    #logger.debug("A debug Statement is executed")
    #logger.info("Some info is printed")
    #logger.warning("This is warning")
    #logger.error("This is an error")
    #logger.critical("There is a critical error")




