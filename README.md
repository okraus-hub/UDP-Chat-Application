# UDP-Chat-Application
This is a lightweight, command-line, peer-to-peer chat application built using Python sockets and UDP. It enables two users to communicate over the network by sending and receiving JSON-formatted messages with sequence tracking for basic message ordering.

Features
-Peer-to-peer communication over UDP
-Threaded message receiving
-Basic message ordering using sequence numbers
-Simple JSON message structure
-Lightweight and easy to use

Requirements
-Python 3.x

Usage
Open two terminal windows (or run on two machines). In each, start the script with:
  python chatP4.py <username> <destination_ip:port> <host_ip:port>

Example (Local Test)
Terminal 1:
  python chatP4.py user1 127.0.0.1:3001 127.0.0.1:2000
Terminal 2:
  python chatP4.py user2 127.0.0.1:2000 127.0.0.1:3001

Message Format
Messages are sent as JSON and include:
-Version: Protocol version (currently "v1")
-Seq. num: Sequence number of the message
-UID: User ID (username)
-DID: Destination ID (IP:port)
-Message: The actual message content

Limitations
-Only supports direct communication between two peers
-No encryption or authentication
-No message retries or acknowledgments

