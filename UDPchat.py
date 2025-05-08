import sys
import json
import socket
import threading

#For local testing: ../chatp4.py user1 127.0.0.1:3001 127.0.0.1:2000 
if len(sys.argv) != 4:
    print("Usage: python chatP4.py <username> <destination_ip:port> <host_ip:port>")
    sys.exit(1)

username = sys.argv[1]
dest_ip, dest_port = sys.argv[2].split(":")
host_ip, host_port = sys.argv[3].split(":")
dest_port, host_port = int(dest_port), int(host_port)

"Set up UDP socket"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host_ip, host_port))

seq_num = 0
expected_seq_num = 0

def receive_messages():
    global expected_seq_num
    while True:
        try:
            data, addr = sock.recvfrom(4096)
            message = json.loads(data.decode())

            if message.get("Seq. num") == expected_seq_num:
                print(f"{message['UID']}>> {message['Message']}")
                expected_seq_num += 1
        except Exception as e:
            print("Error recieving message:", e)

#Start the recieving thread
receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

print(f"{username} is now online. Type messages below:")

#Sending messages
while True:
    try:
        msg = input().strip()
        if not msg:
            continue

        message_dict = {
            "Version": "v1",
            "Seq. num": seq_num,
            "UID": username,
            "DID": sys.argv[2],
            "Message": msg,
        }

        sock.sendto(json.dumps(message_dict).encode(), (dest_ip, dest_port))
        seq_num += 1
    except KeyboardInterrupt:
        print("\nExiting chat...")
        break
    except Exception as e:
        print("Error sending message:", e)
    
sock.close()
