from typing import List


class Spot:
    """
    Place where a transportation can go.
    """
    def __init__(self, address: str, identifier: str = "", baggage: str = ""):
        """

        :param address: address of place
        :param identifier: some specific identifier eg. gate 43 at airport, train platform 2
        :param baggage: place where baggage can be left
        """
        self.address = address
        self.identifier = identifier
        self.baggage = baggage

