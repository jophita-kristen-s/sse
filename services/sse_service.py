import queue

# Stores connected users
# Format:
# {
#    user_id : Queue()
# }
clients = {}


def add_client(user_id):
    """
    Create a queue for a newly connected user
    """

    client_queue = queue.Queue()

    clients[user_id] = client_queue

    return client_queue


def remove_client(user_id):
    """
    Remove disconnected user
    """

    if user_id in clients:
        del clients[user_id]


def send_to_user(receiver_id, message):
    """
    Send message to a specific user
    """

    receiver_id = str(receiver_id)

    if receiver_id in clients:
        clients[receiver_id].put(message)


def broadcast(message):
    """
    Send message to all connected users
    """

    for client_queue in clients.values():
        client_queue.put(message)


def get_connected_users():
    """
    Return connected users list
    """

    return list(clients.keys())