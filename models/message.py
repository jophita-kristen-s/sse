from db import db
from datetime import datetime

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    sender = db.Column(
        db.String(20),
        nullable=False
    )

    receiver = db.Column(
        db.String(20),
        nullable=False
    )

    text = db.Column(
        db.Text,
        nullable=False
    )

    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )