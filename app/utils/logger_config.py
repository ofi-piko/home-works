import sys
import logging

def setup_logger():
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.DEBUG,
        format='%(asctime)s | %(levelname)s | %(name)s -> %(message)s',
        datefmt="%H:%M:%S"
    )