import logging


class Consummer:
    def __init__(self, *providers):
        self.providers = providers

    def scrape(self):
        export = {}
        for provider in self.providers:
            try:
                export[provider.name] = provider.scrape()
            except (NotImplementedError):
                logging.error(
                    f"{type(provider).__name__} does not have the function scrape() implemented"
                )
        return export
