import logging


class Consummer:
    def __init__(self, *providers):
        self.providers = providers

    def scrape(self):
        for provider in self.providers:
            try:
                provider.scrape()
            except (NotImplementedError):
                logging.error(
                    f"{type(provider).__name__} does not have the function scrape() implemented"
                )
