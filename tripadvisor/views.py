from marshmallow import ValidationError
from flask import request, Blueprint
from flask.views import MethodView

from tripadvisor.schema import boarding_cards_stack_schema


bp_boardin_cards = Blueprint('boardin_cards', __name__)


class BoardingCardsAPI(MethodView):
    def post(self):
        try:
            data_in = boarding_cards_stack_schema.load(request.json)
        except ValidationError as e:
            return e.messages, 400
        data_out = boarding_cards_stack_schema.dump(data_in)
        return data_out


bp_boardin_cards.add_url_rule(
    'BoardingCards/sort', view_func=BoardingCardsAPI.as_view('boarding_cards')
)
