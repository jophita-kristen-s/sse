class Config:

    SECRET_KEY = "secret-key"

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:password@localhost/chatdb"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False