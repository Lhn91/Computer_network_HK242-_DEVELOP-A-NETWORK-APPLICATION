import socket
import threading

def establish_peer_connection(peer_address):
    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peer_socket.connect(peer_address)
    return peer_socket

def send_message(peer_connection, message):
    peer_connection.send(message.encode())

def receive_message(peer_connection):
    try:
        message = peer_connection.recv(1024).decode()
        return message
    except Exception as e:
        print(f"Error receiving message: {e}")
        return None

def handle_disconnection(peer_connection):
    peer_connection.close()

def broadcast_message(peers, message):
    for peer in peers:
        try:
            send_message(peer, message)
        except Exception as e:
            print(f"Error sending message to peer: {e}")

def listen_for_connections(host, port, on_new_connection):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(10)
    while True:
        peer_socket, peer_address = server_socket.accept()
        threading.Thread(target=on_new_connection, args=(peer_socket, peer_address)).start()

def start_p2p_communication(host, port, on_new_connection):
    threading.Thread(target=listen_for_connections, args=(host, port, on_new_connection)).start()