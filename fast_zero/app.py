from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message

app = FastAPI(title='Curso Fast Zero')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo'}
