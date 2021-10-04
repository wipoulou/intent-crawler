import logging

from consumer import Consummer
from providers import auchan, carrefour, franprix, lidl

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename="output.log",
    encoding="utf-8",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

if __name__ == "__main__":
    logging.info("Starting")

    consumer = Consummer(
        auchan.auchan,
        carrefour.carrefour,
        franprix.franprix,
        lidl.lidl,
    )

    consumer.scrape()
    logging.info("Ending")
