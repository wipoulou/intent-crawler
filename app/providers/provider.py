class Provider:
    name = None
    endpoint = None

    def scrape(self) -> dict:
        raise NotImplementedError
