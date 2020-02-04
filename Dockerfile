FROM python:3.7

WORKDIR /usr/src/

RUN pip install pipenv
COPY Pipfile ./
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
COPY tripadvisor /usr/src/tripadvisor

ENV FLASK_APP tripadvisor


EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]