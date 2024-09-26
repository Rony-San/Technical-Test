from flask import Flask
from app.routes import init_routes
from app.handlers.error_handlers import register_error_handlers

def create_app():
    app = Flask(__name__)

    init_routes(app)

    register_error_handlers(app)

    return app
