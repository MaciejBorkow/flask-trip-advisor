import pytest
from marshmallow import ValidationError

from tripadvisor.schema import BoardingCardsStackSchema


def test_valid_boarding_cards_stack_schema(valid_boarding_card_stack_from_recruitment_task):
    output = [
        "Take train 78A from Madrid to Barcelona. Sit in seat 45B.",
        "Take the airport bus from Barcelona to Girona Airport. No seat assignment.",
        "From Girona Airport, take flight SK455 to Stockholm. Gate 45B, seat 3A. Baggage drop at ticket counter 344.",
        "From Stockholm, take flight SK22 to New York JFK. Gate 22, seat 7B. Baggage will we automatically transferred from your last leg."
    ]
    deserialized_obj = BoardingCardsStackSchema().load(valid_boarding_card_stack_from_recruitment_task)

    assert deserialized_obj.stack[0].verbose == output[0]
    assert deserialized_obj.stack[1].verbose == output[1]
    assert deserialized_obj.stack[2].verbose == output[2]
    assert deserialized_obj.stack[3].verbose == output[3]