from provider import Provider

"""
Franprix has an API, so it doesn't fit the scrapping requirement, but still interesting to get the data.
"""


class Franprix(Provider):
    name = "Franprix"
    endpoint = ""


franprix = Franprix()
