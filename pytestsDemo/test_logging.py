import logging


def test_logging():
    logger = logging.getLogger(__name__)  # it will automatically get the file name

    file_handler = logging.FileHandler('logfile.log')  # defined where to log
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # defined the format
    file_handler.setFormatter(formatter)  # connected the formatter with the file handler.
    # Now file handler has the format information.

    logger.addHandler(file_handler)  # connected it with the file handler.

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")
