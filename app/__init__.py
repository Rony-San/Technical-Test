from flask import Flask
from app.routes import init_routes
from app.handlers.error_handlers import register_error_handlers
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(
            app,
            resources={r"/*": {"origins": "*"}},
            supports_credentials=True,
            allow_headers=["X-Webhook-Token", "Content-Type"],
        )
    init_routes(app)
    register_error_handlers(app)

 
    return app
