class Config:

    SECRET_KEY = "secret-key"

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:pattu&123@localhost/chatdb"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False