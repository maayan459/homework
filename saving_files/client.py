import socket

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8080))

with open("C://Users\maaya//.vscode//homework-new//client.py", "rb") as file:
    while True:
        data=file.read(1024)
        if not data:
            break
        client_socket.send(data)
    print("finish with sending")

print("proccess comlplete")