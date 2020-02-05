from abc import ABC, abstractmethod


class AbstractSerializer(ABC):
    @abstractmethod
    def from_to(self, departure, destination, transportation):
        pass

    @abstractmethod
    def where_start_and_seat(self, transportation):
        pass

    @abstractmethod
    def baggage(self, transportation):
        pass

    @abstractmethod
    def to_str(self):
        pass


class TrainSerializer(AbstractSerializer):
    def __init__(self):
        self._verbose = None

    def from_to(self, departure, destination, transportation):
        article = "" if self.transportation.identifier else "the "
        self._verbose = f"Take {article}{transportation.description} {transportation.category} " \
                        f"{transportation.identifier} from {departure.address} to {destination.address}."

    def where_start_and_seat(self, transportation):
        self._verbose += f" Sit in seat {transportation.seat}" if transportation.seat else " No seat assignment."

    def baggage(self, transportation):
        self._verbose += f" Baggage drop at {transportation.baggage}." if transportation.baggage else ""

    def to_str(self):
        return self._verbose


class BusSerializer(AbstractSerializer):
    def __init__(self):
        self._verbose = None

    def from_to(self, departure, destination, transportation):
        article = "" if self.transportation.identifier else "the "
        self._verbose = f"Take {article}{transportation.description} {transportation.category} " \
                        f"{transportation.identifier} from {departure.address} to {destination.address}."

    def where_start_and_seat(self, transportation):
        self._verbose += f" Sit in seat {transportation.seat}" if transportation.seat else " No seat assignment."

    def baggage(self, transportation):
        self._verbose += f" Baggage drop at {transportation.baggage}." if transportation.baggage else ""

    def to_str(self):
        return self._verbose


class FlightSerializer(AbstractSerializer):
    def __init__(self):
        self._verbose = None

    def from_to(self, departure, destination, transportation):
        self._verbose = f"From {departure.address}, take {transportation.category} to {destination.address}."

    def where_start_and_seat(self, transportation):
        self._verbose += f" Gate {transportation.identifier}, seat {transportation.seat}"

    def baggage(self, transportation):
        if self.transportation.baggage:
            self._verbose += f" Baggage drop at ticket counter {transportation.baggage}."
        else:
            self._verbose += " Baggage will we automatically transferred from your last leg."

    def to_str(self):
        return self._verbose


class SerializerFactory:
    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()
factory.register_format('train', TrainSerializer)
factory.register_format('bus', BusSerializer)
factory.register_format('flight', FlightSerializer)


class BoardingCardDescriptionSerializer:
    """
    Serialize boarding card base on transportation category ("train", "bus" etc)
    """
    def serialize(self, serializable, category):
        serializer = factory.get_serializer(category)
        serializable.serialize(serializer)
        return serializer.to_str()
