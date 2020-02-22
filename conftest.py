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


@pytest.fixture
def valid_boarding_card_stack_from_recruitment_task():

    boarding_card_stack_dict = {
        "stack": [
        {
            "transportation": {
                'category': 'train',
                'description': '',
                'identifier': '78A',
                'seat': '45B',
                'baggage': ''
            },
            "departure": {
                "address": "Madrid",
                "identifier": "",
            },
            "destination": {
                "address": "Barcelona",
                "identifier": "",
            }
        },
        {
            "transportation": {
                'category': 'bus',
                'description': 'airport',
                'identifier': '',
                'seat': '',
                'baggage': ''
            },
            "departure": {
                "address": "Barcelona",
                "identifier": "",
            },
            "destination": {
                "address": "Girona Airport",
                "identifier": "",
            }
        },
        {
            "transportation": {
                'category': 'flight',
                'description': '',
                'identifier': 'SK455',
                'seat': '3A',
                'baggage': '344'
            },
            "departure": {
                "address": "Girona Airport",
                "identifier": "45B",
            },
            "destination": {
                "address": "Stockholm",
                "identifier": "",
            }
        },
        {
            "transportation": {
                'category': 'flight',
                'description': '',
                'identifier': 'SK22',
                'seat': '7B',
                'baggage': ''
            },
            "departure": {
                "address": "Stockholm",
                "identifier": "22",
            },
            "destination": {
                "address": "New York JFK",
                "identifier": "",
            }
        }
        ]
    }

    return copy.deepcopy(boarding_card_stack_dict)
