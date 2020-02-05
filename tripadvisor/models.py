from typing import List

from tripadvisor.serializers import BoardingCardDescriptionSerializer

class Spot:
    """
    Place where a transportation can go.
    """
    def __init__(self, address: str, identifier: str = "", baggage: str = ""):
        """
        :param address: address of place
        :param identifier: some specific identifier eg. gate 43 at airport, train platform 2
        """
        self.address = address
        self.identifier = identifier


class Transportation:
    """
    Transportation to move from A to B.
    """

    categories = ['train', 'flight', 'bus']  # acceptable types of transportation

    def __init__(self, category: categories, description: str = "", identifier: str = "", seat: str = "", baggage=""):
        """
        :param category: on of acceptable transportation type from Class variable 'categories'
        :param description: additional information eg. city (for bus), charter (for flight)
        :param identifier: to help find the transportation eg. bus plates, plain number
        :param seat: place where to sit during locomotion
        :param baggage: where to leave
        """
        self.category = category
        self.description = description
        self.identifier = identifier
        self.seat = seat
        self.baggage = baggage

class BoardingCard:
    _serializer = BoardingCardDescriptionSerializer()
    """
    BoardingCard describing how to get from Spot A to B by a Transportation
    """
    def __init__(self, transportation: Transportation, departure: Spot, destination: Spot):
        """Look to objects description from type hints."""
        self.transportation = transportation
        self.departure = departure
        self.destination = destination
        self.verbose = BoardingCard._serializer.serialize(self, self.transportation.category)

    # @property
    # def verbose(self):
    #     if not self.verbose:
    #         self.verbose = BoardingCard._serializer.serialize(self, self.transportation.category)
    #     return self.verbose

    def serialize(self, serializer):
        serializer.from_to(self.departure, self.destination, self.transportation)
        serializer.where_start_and_seat(self.transportation, self.departure)
        serializer.baggage(self.transportation.baggage)


class BoardingCardsStack:
    """Represent BoardingCards list and give interface to operate on them."""
    def __init__(self, stack: List[BoardingCard]):
        self.stack = stack

    def sort(self):
        """
        Sort boarding cards stack.
        """
        pass
