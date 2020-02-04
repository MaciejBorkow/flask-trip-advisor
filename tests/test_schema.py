import pytest
from marshmallow import ValidationError

from tripadvisor.schema import SpotScheme, TransportationSchema
from tripadvisor.models import Spot, Transportation, BoardingCard, BoardingCardsStack


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

