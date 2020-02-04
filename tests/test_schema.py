import pytest
from marshmallow import ValidationError

from tripadvisor.schema import SpotScheme, TransportationSchema, BoardingCardSchema, BoardingCardsStackSchema
from tripadvisor.models import BoardingCard


def test_valid_spot_schema():
    valid_dict = {
        "address": "Dworzec Głowny, Poznan, Poland",
        "identifier": "peron 7",
        "baggage": "u kierowcy"
    }
    assert SpotScheme().load(valid_dict).__dict__ == valid_dict
    del valid_dict['identifier']
    del valid_dict['baggage']
    deserialized_obj = SpotScheme().load(valid_dict)
    assert deserialized_obj.address == valid_dict['address']
    assert not deserialized_obj.identifier and not deserialized_obj.baggage


def test_not_valid_spot_schema():
    not_valid_dict = {
        "address": "Dworzec Głowny, Poznan, Poland",
        "id": "",
        "baggage": 1
    }
    ValidationError_message_dict = {
        'id': ['Unknown field.'],
        'baggage': ['Not a valid string.'],
    }
    with pytest.raises(ValidationError) as errinfo:
        SpotScheme().load(not_valid_dict).load(not_valid_dict)
    assert ValidationError_message_dict == errinfo.value.messages


def test_valid_transportation_schema():
    valid_dict = {
        'category': 'train',
        'description': 'airport',
        'identifier': '123'
    }
    assert TransportationSchema().load(valid_dict).__dict__ == valid_dict


def test_not_valid_transportation_schema():
    not_valid_dict = {
        'category': 'trainaa',
        'description': None,
        'identifier': 1
    }
    ValidationError_message_dict = {
        'category': ['Must be one of: train, flight, bus.'],
        'description': ['Field may not be null.'],
        'identifier': ['Not a valid string.']
    }
    with pytest.raises(ValidationError) as errinfo:
        TransportationSchema().load(not_valid_dict)
    assert ValidationError_message_dict == errinfo.value.messages


def test_valid_boarding_card_schema(valid_boarding_card_stack):
    valid_dict = valid_boarding_card_stack["stack"][0]
    deserialized_obj = BoardingCardSchema().load(valid_dict)
    assert isinstance(deserialized_obj, BoardingCard)
    assert deserialized_obj.transportation.__dict__ == valid_dict["transportation"]
    assert deserialized_obj.departure.__dict__ == valid_dict["departure"]
    assert deserialized_obj.destination.__dict__ == valid_dict["destination"]


def test_not_valid_boarding_card_schema(valid_boarding_card_stack):
    not_valid_dict = valid_boarding_card_stack["stack"][0]
    del not_valid_dict['transportation']
    del not_valid_dict['departure']
    not_valid_dict['random_key'] = 'random_value'
    not_valid_dict['destination'] = 1
    ValidationError_message_dict = {
        'departure': ['Missing data for required field.'],
        'transportation': ['Missing data for required field.'],
        'random_key': ['Unknown field.'],
        'destination': {'_schema': ['Invalid input type.']},
    }
    with pytest.raises(ValidationError) as errinfo:
        BoardingCardSchema().load(not_valid_dict)
    assert ValidationError_message_dict == errinfo.value.messages


def test_valid_boarding_cards_stack_schema(valid_boarding_card_stack):
    deserialized_obj = BoardingCardsStackSchema().load(valid_boarding_card_stack)

    assert deserialized_obj.stack[0].transportation.__dict__ == valid_boarding_card_stack["stack"][0]['transportation']
    assert deserialized_obj.stack[0].destination.__dict__ == valid_boarding_card_stack["stack"][0]['destination']
    assert deserialized_obj.stack[0].departure.__dict__ == valid_boarding_card_stack["stack"][0]['departure']
