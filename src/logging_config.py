import logging

def setup_logging():
    logging.basicConfig(
        filename="logs/etl.log", 
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )