import logging

from consumer import Consummer
from provider import Provider

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename="output.log",
    encoding="utf-8",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

if __name__ == "__main__":
    logging.info("Starting")
    provider1 = Provider("test.com")
    provider2 = Provider("test.fr")
    consumer = Consummer(provider1, provider2)

    consumer.scrape()
    logging.info("Ending")
