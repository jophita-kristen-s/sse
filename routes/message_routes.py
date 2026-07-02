from flask import Blueprint, Response, request, jsonify
from services.sse_service import (
    add_client,
    remove_client
)
from services.message_service import process_message

from models.message import Message

import json

message_bp = Blueprint(
    "message",
    __name__
)


# SSE connection endpoint
@message_bp.route("/stream/<user_id>")
def stream(user_id):

    client_queue = add_client(user_id)

    def event_stream():

        try:
            while True:

                message = client_queue.get()

                yield (
                    f"data:{json.dumps(message)}\n\n"
                )

        except GeneratorExit:

            remove_client(user_id)

    return Response(
        event_stream(),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
        }
    )


# Send API
@message_bp.route(
    "/send",
    methods=["POST"]
)
def send():

    data = request.json

    message = process_message(
        data["sender"],
        data["receiver"],
        data["text"]
    )

    return jsonify(message)


@message_bp.route(
    "/send/<sender>/<receiver>/<text>",
    methods=["GET"]
)
def send_get(sender, receiver, text):

    message = process_message(
        sender,
        receiver,
        text
    )

    return jsonify(message)


# Get all messages
@message_bp.route("/messages", methods=["GET"])
def get_messages():

    messages = Message.query.order_by(Message.timestamp).all()

    return jsonify([
        {
            "id": m.id,
            "sender": m.sender,
            "receiver": m.receiver,
            "text": m.text,
            "timestamp": m.timestamp.isoformat()
        }
        for m in messages
    ])

