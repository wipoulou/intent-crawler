class Provider:
    def __init__(self, url):
        self.urf = url

    def scrape(self) -> dict:
        raise NotImplementedError
