from fastapi import FastAPI

app = FastAPI(title='Curso Fast Zero')


@app.get('/')
def read_root():
    return {'message': 'Olá mundo'}
