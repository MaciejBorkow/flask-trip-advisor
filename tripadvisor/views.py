from marshmallow import ValidationError
from flask import request, Blueprint
from flask.views import MethodView


bp_boardin_cards = Blueprint('boardin_cards', __name__)


class BoardingCardsAPI(MethodView):
    def post(self):

        return {'data': 'init data'}


bp_boardin_cards.add_url_rule(
    'BoardingCards/sort', view_func=BoardingCardsAPI.as_view('boarding_cards')
)
