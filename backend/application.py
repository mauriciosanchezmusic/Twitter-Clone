"""Application module.

from fastapi import FastAPI

from .containers import Container
from .View.Endpoint_Admin import endpointAdmin
from .View.Endpoint_Status import endpointStatus
from .View.Endpoint_User import endpointUser


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(endpointAdmin.router)
    app.include_router(endpointStatus.router)
    app.include_router(endpointUser.router)
    return app


app = create_app()
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True) # debug=True restarts the server everytime we make a change in our code
