from flask import Flask
from config import Config
from db import db
from routes.message_routes import message_bp
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(message_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(
        debug=True,
        threaded=True
    )

