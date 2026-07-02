from models.message import Message
from db import db
from services.sse_service import send_to_user
#from services.sse_service import send_to_user


def process_message(sender, receiver, text):

    message = Message(
        sender=sender,
        receiver=receiver,
        text=text
    )

    db.session.add(message)
    db.session.commit()

    payload = {
        "id": message.id,
        "sender": sender,
        "receiver": receiver,
        "text": text,
        "timestamp": message.timestamp.isoformat()
    }

    
    send_to_user(receiver, payload)
    send_to_user(sender, payload)
    
    return payload