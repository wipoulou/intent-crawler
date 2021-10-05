import logging

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename="output.log",
    encoding="utf-8",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

if __name__ == "__main__":
    logging.info("Starting")

    logging.info("Ending")
