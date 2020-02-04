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

class BoardingCard:
    """
    BoardingCard describing how to get from Spot A to B by a Transportation
    """
    def __init__(self, transportation: Transportation, departure: Spot, destination: Spot):
        """Look to objects description from type hints."""
        self.transportation = transportation
        self.departure = departure
        self.destination = destination
        self.verbose = self._serialize()

    def _serialize(self):
        """
        Serialize boarding verbose description readable for humans.
        :return: verbose description
        """
        return ""


class BoardingCardsStack:
    """Represent BoardingCards list and give interface to operate on them."""
    def __init__(self, stack: List[BoardingCard]):
        self.stack = stack

    def sort(self):
        """
        Sort boarding cards stack.
        """
        pass
