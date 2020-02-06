# Tripadvisor

Flask app to plan a trip by sorting boarding cards.

## Running Docker image

- Mount Docker image:

    `sudo docker build -t tripadvisor .`

- Run Docker image:

    `sudo docker run -p 5000:5000 tripadvisor`

- Service is on 0.0.0.0:5000 now.

## Runing the tests

- Enter project path where the Pipfile is.

- Install virtual environment with pipenv package.

    `python -m pipenv install`

- Activate virtual environment.

    `python -m pipenv shell`

- Run tests:

    `pytest`

## API


- Sort posted boarding cards and return verbose trip description:

    - POST `/api/boardingcards`
    
 Example json with data from task description:
 
 ```json
    {
        "stack": [
        {
            "transportation": {
                "category": "train",
                "description": "",
                "identifier": "78A",
                "seat": "45B",
                "baggage": ""
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
                "category": "bus",
                "description": "airport",
                "identifier": "",
                "seat": "",
                "baggage": ""
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
                "category": "flight",
                "description": "",
                "identifier": "SK455",
                "seat": "3A",
                "baggage": "344"
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
                "category": "flight",
                "description": "",
                "identifier": "SK22",
                "seat": "7B",
                "baggage": ""  {
        "stack": [
        {
            "transportation": {
                "category": "train",
                "description": "",
                "identifier": "78A",
                "seat": "45B",
                "baggage": ""
            },
            "departure": {
                "address": "Madrid",
                "identifier": ""
            },
            "destination": {
                "address": "Barcelona",
                "identifier": ""
            }
        },
        {
            "transportation": {
                "category": "bus",
                "description": "airport",
                "identifier": "",
                "seat": "",
                "baggage": ""
            },
            "departure": {
                "address": "Barcelona",
                "identifier": ""
            },
            "destination": {
                "address": "Girona Airport",
                "identifier": ""
            }
        },
        {
            "transportation": {
                "category": "flight",
                "description": "",
                "identifier": "SK455",
                "seat": "3A",
                "baggage": "344"
            },
            "departure": {
                "address": "Girona Airport",
                "identifier": "45B"
            },
            "destination": {
                "address": "Stockholm",
                "identifier": ""
            }
        },
        {
            "transportation": {
                "category": "flight",
                "description": "",
                "identifier": "SK22",
                "seat": "7B",
                "baggage": ""
            },
            "departure": {
                "address": "Stockholm",
                "identifier": "22"
            },
            "destination": {
                "address": "New York JFK",
                "identifier": ""
            }
        }
        ]
    }
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
```    