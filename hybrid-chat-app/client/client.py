import socket
import threading
import argparse

class ChatClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.peers = []

    def connect_to_server(self):
        self.client_socket.connect((self.server_ip, self.server_port))
        print(f"Connected to server at {self.server_ip}:{self.server_port}")
        threading.Thread(target=self.listen_for_messages).start()

    def listen_for_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print(message)
            except Exception as e:
                print("Error receiving message:", e)
                break

    def send_message(self, channel, message):
        self.client_socket.send(f"{channel}: {message}".encode())

    def submit_peer_info(self, peer_info):
        self.send_message("SYSTEM", f"NEW_PEER {peer_info}")

    def broadcast_message(self, channel, message):
        self.send_message(channel, message)

def main():
    parser = argparse.ArgumentParser(description='Chat Client')
    parser.add_argument('--server-ip', required=True, help='IP address of the server')
    parser.add_argument('--server-port', type=int, required=True, help='Port of the server')
    args = parser.parse_args()

    client = ChatClient(args.server_ip, args.server_port)
    client.connect_to_server()

    while True:
        channel = input("Enter channel: ")
        message = input("Enter message to send: ")
        client.broadcast_message(channel, message)

if __name__ == "__main__":
    main()