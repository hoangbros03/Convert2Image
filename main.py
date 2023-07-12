import logging

logging.basicConfig(
    filemode="a",
    filename="log.log",
    format="%(asctime)s - %(message)s",
    level=logging.DEBUG,
)
logging.info("Test")
