from typing import List
from _collections import deque

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
        self._verbose = ""

    @property
    def verbose(self):
        if not self._verbose:
            self._verbose = BoardingCard._serializer.serialize(self, self.transportation.category)
        return self._verbose

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
        l_nodes = [(obj.departure.address, obj.destination.address) for obj in self.stack]
        l_nodes_in = [obj.departure.address for obj in self.stack]
        l_nodes_out = [obj.destination.address for obj in self.stack]

        def find_nodes(ind_sort, previous=False):
            if previous:
                base_node_to_compare = l_nodes_in[ind_sort[0]]
                node_indx_to_iter = l_nodes_out
            else:
                base_node_to_compare = l_nodes_out[ind_sort[-1]]
                node_indx_to_iter = l_nodes_in
            nodes_index = [ni for ni, n in enumerate(node_indx_to_iter) if
                           n == base_node_to_compare and ni not in ind_sort]

            if nodes_index and previous:
                ind_sort.appendleft(nodes_index[0])
                return find_nodes(ind_sort, previous=True)
            elif nodes_index and not previous:
                ind_sort.append(nodes_index[0])
                return find_nodes(ind_sort)
            elif len(ind_sort) < len(l_nodes) and not previous:
                return find_nodes(ind_sort, previous=True)
            elif len(ind_sort) == len(l_nodes):
                return ind_sort
            else:
                return ind_sort

        indexes_sorted = find_nodes(deque([0]))
        self.stack = [self.stack[i] for i in indexes_sorted]
