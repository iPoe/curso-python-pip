import store

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
    <html>
        <head>
            <title> Crane AI</title>
        </head>
        <body>
            <h1>Hola, gracias por querer contactarnos</h1>
        <body>
    </html>
    """

@app.get('/landing', response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title> Crane AI</title>
        </head>
        <body>
            <h1>Servicios a tu medida</h1>
        <body>
    </html>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()
