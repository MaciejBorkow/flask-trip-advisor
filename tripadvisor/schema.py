from marshmallow import Schema, fields, validate, post_load
from tripadvisor.models import Spot, Transportation, BoardingCard, BoardingCardsStack


class SpotScheme(Schema):
    address = fields.Str(required=True, validate=validate.Length(min=3, max=200))
    identifier = fields.Str(validate=validate.Length(max=200))
    baggage = fields.Str(validate=validate.Length(max=200))

    @post_load
    def make_object(self, data, **kwargs):
        return Spot(**data)


class TransportationSchema(Schema):
    category = fields.Str(required=True, validate=validate.OneOf(Transportation.categories))
    description = fields.Str(validate=validate.Length(max=200))
    identifier = fields.Str(validate=validate.Length(max=200))

    @post_load
    def make_object(self, data, **kwargs):
        return Transportation(**data)

