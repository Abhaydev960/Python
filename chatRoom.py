# Save as chat_room.py
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                break
            print("\nFriend:", message)
        except OSError:
            break
# Select server or client mode
mode = input("Start as server or client? (s/c): ").lower()
if mode == "s":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print("Server waiting for a friend...")
    conn, address = server.accept()
    chat = conn

    print("Friend connected:", address)
else:
    chat = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    chat.connect((HOST, PORT))

    print("Connected to chat room.")
# Start receiving messages in a separate thread
thread = threading.Thread(
    target=receive_messages,
    args=(chat,),
    daemon=True
)
thread.start()
print("Type /quit to leave.")
# Send messages
while True:
    message = input("You: ")
    if message == "/quit":
        break
    try:
        chat.sendall(message.encode())
    except OSError:
        print("Connection closed.")
        break
