from flask import Blueprint
from app.routes.app_routes import main

def init_routes(app):
    app.register_blueprint(main)
