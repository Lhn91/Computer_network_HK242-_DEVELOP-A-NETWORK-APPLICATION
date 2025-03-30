# Hybrid Chat Application

## Overview
The Hybrid Chat Application is a versatile chat solution that combines both client-server and peer-to-peer (P2P) communication paradigms. This application allows users to connect to a centralized server for initial communication and then switch to direct peer-to-peer connections for enhanced interaction and live streaming capabilities.

## Project Structure
```
hybrid-chat-app
├── client
│   ├── client.py        # Client-side implementation
│   └── __init__.py      # Package initialization
├── server
│   ├── server.py        # Centralized server implementation
│   └── __init__.py      # Package initialization
├── p2p
│   ├── p2p.py           # Peer-to-peer communication logic
│   └── __init__.py      # Package initialization
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd hybrid-chat-app
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Server**
   Start the server by executing:
   ```bash
   python server/server.py
   ```

4. **Run the Client**
   In a new terminal, start the client:
   ```bash
   python client/client.py --server-ip <server-ip> --server-port <server-port>
   ```

## Usage Guidelines
- Connect multiple clients to the server to start chatting.
- Use the peer-to-peer functionality for direct communication between clients.
- Follow the prompts in the client application to send messages and manage connections.

## Additional Information
- Ensure that the server is running before starting any clients.
- Modify the `requirements.txt` file to include any additional libraries as needed for your development.

## License
This project is licensed under the MIT License - see the LICENSE file for details.