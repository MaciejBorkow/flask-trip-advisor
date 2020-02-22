from marshmallow import Schema, fields, validate, post_load, post_dump, pre_dump
from tripadvisor.models import Spot, Transportation, BoardingCard, BoardingCardsStack


class SpotScheme(Schema):
    address = fields.Str(required=True, validate=validate.Length(min=3, max=200))
    identifier = fields.Str(validate=validate.Length(max=200))

    @post_load
    def make_object(self, data, **kwargs):
        return Spot(**data)


class TransportationSchema(Schema):
    category = fields.Str(required=True, validate=validate.OneOf(Transportation.categories))
    description = fields.Str(validate=validate.Length(max=200))
    identifier = fields.Str(validate=validate.Length(max=200))
    seat = fields.Str(validate=validate.Length(max=200))
    baggage = fields.Str(validate=validate.Length(max=200))

    @post_load
    def make_object(self, data, **kwargs):
        return Transportation(**data)


class BoardingCardSchema(Schema):
    transportation = fields.Nested(TransportationSchema, required=True, load_only=True)
    departure = fields.Nested(SpotScheme, required=True, load_only=True)
    destination = fields.Nested(SpotScheme, required=True, load_only=True)
    verbose = fields.Str(dump_only=True, required=True)

    @post_load
    def make_object(self, data, **kwargs):
        return BoardingCard(**data)


class BoardingCardsStackSchema(Schema):
    stack = fields.List(fields.Nested(BoardingCardSchema))

    @post_load
    def make_object(self, data, **kwargs):
        return BoardingCardsStack(**data)


boarding_cards_stack_schema = BoardingCardsStackSchema()
