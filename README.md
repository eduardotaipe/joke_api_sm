# Squad Makers API

Technical challenge of Jokes and Maths APIs.

## Installation

- Clone repository.
```bash
git clone https://github.com/eduardotaipe/joke_api_sm.git
```
- Install dependencies.
```bash
cd joke_api_sm
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Run app.
```bash
export PYTHONPATH=$PWD
python app/main.py
```

## EndPoints

- Joke:
```
GET http://127.0.0.1:8000/api/v1/joke/
GET http://127.0.0.1:8000/api/v1/joke/{name_api}
POST http://127.0.0.1:8000/api/v1/joke/
PUT http://127.0.0.1:8000/api/v1/joke/{id}
DELETE http://127.0.0.1:8000/api/v1/joke/{id}
```
- Math:
```
http://127.0.0.1:8000/api/v1/math/lcm?numbers={comma_separated_integers}'
http://127.0.0.1:8000/api/v1/math/plus_one?number={integer}'
```
## Usage

For the JokeAPI you can use the interactive api documentation from [here](http://127.0.0.1:8000/docs).


For the MathAPI LCM(Lowest Common Multiple) Fastapi does not format the url correctly, use CURL or any other tool to test this endpoint.

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/math/lcm?numbers=15,30,2,4' \
  -H 'accept: application/json'
```

## Test

- Run tests.
```bash
pytest
```