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

TODO