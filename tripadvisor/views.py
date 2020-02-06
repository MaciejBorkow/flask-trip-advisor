from marshmallow import ValidationError
from flask import request, Blueprint
from flask.views import MethodView

from tripadvisor.schema import boarding_cards_stack_schema


bp_boardin_cards = Blueprint('boardin_cards', __name__)


class BoardingCardsAPI(MethodView):
    def post(self):
        try:
            boarding_cards_stack = boarding_cards_stack_schema.load(request.json)
        except ValidationError as e:
            return e.messages, 400
        boarding_cards_stack.sort()
        data_out = boarding_cards_stack_schema.dump(boarding_cards_stack)
        data_out['stack'].append({'verbose': 'You have arrived at your final destination.'})
        return data_out


bp_boardin_cards.add_url_rule(
    'boardingcards', view_func=BoardingCardsAPI.as_view('boarding_cards')
)
