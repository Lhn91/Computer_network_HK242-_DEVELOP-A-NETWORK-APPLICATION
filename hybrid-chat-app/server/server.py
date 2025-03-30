import socket
from threading import Thread

class ChatServer:
    def __init__(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(10)
        self.clients = []
        self.channels = {}  # Dictionary to store channels and their messages

    def broadcast(self, message, client_socket, channel):
        for client in self.clients:
            if client != client_socket:
                try:
                    client.send(f"{channel}: {message}".encode())
                except Exception:
                    self.clients.remove(client)

    def handle_client(self, client_socket, address):
        print(f"Connection from {address} has been established.")
        self.clients.append(client_socket)
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                # Assuming the message format is "channel: message"
                channel, msg = message.split(": ", 1)
                if channel not in self.channels:
                    self.channels[channel] = []
                self.channels[channel].append(msg)
                self.broadcast(msg, client_socket, channel)
            except Exception:
                break
        client_socket.close()
        self.clients.remove(client_socket)
        print(f"Connection from {address} has been closed.")

    def start(self):
        print("Server is listening...")
        while True:
            client_socket, address = self.server_socket.accept()
            client_thread = Thread(target=self.handle_client, args=(client_socket, address))
            client_thread.start()

if __name__ == "__main__":
    host = '0.0.0.0'  # Listen on all interfaces
    port = 22236
    chat_server = ChatServer(host, port)
    chat_server.start()