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


class Transportation:
    """
    Transportation to move from A to B.
    """

    categories = ['train', 'flight', 'bus']  # acceptable types of transportation

    def __init__(self, category: categories, description: str = "", identifier: str = ""):
        """
        :param category: on of acceptable transportation type from Class variable 'categories'
        :param description: additional information eg. city (for bus), charter (for plain)
        :param identifier: to help find the transportation eg. bus plates, plain number
        """
        self.category = category
        self.description = description
        self.identifier = identifier

