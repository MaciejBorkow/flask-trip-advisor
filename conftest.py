import copy
import pytest
from tripadvisor import create_app


@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    return app


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def valid_boarding_card_stack():

    boarding_card_stack_dict = {
        "stack": [{
            "transportation": {
                'category': 'train',
                'description': 'airport',
                'identifier': '123',
                'seat': '32A',
                'baggage': '123'
            },
            "departure": {
                "address": "Dworzec Głowny, Poznan, Poland",
                "identifier": "peron 7",
            },
            "destination": {
                "address": "Dworzec Głowny, Warszawa, Poland",
                "identifier": "peron 12",
            }
        },
        {
            "transportation": {
                'category': 'train',
                'description': 'airport',
                'identifier': '123',
                'seat': '32A',
                'baggage': '123'
            },
            "departure": {
                "address": "Dworzec Głowny, Poznan, Poland",
                "identifier": "peron 7",
            },
            "destination": {
                "address": "Dworzec Głowny, Warszawa, Poland",
                "identifier": "peron 12",
            }
        }]
    }

    return copy.deepcopy(boarding_card_stack_dict)
