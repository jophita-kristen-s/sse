import os


class Config:

    SECRET_KEY = "secret-key"

    """SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:password@localhost/chatdb"
    )"""

    DATABASE_URL = os.environ.get("DATABASE_URL")

    SQLALCHEMY_TRACK_MODIFICATIONS = False