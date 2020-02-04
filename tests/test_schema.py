import pytest
from marshmallow import ValidationError

from tripadvisor.schema import SpotScheme
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

