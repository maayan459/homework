import socket
def get_file(file_name, host, port):
  try:

    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen(1)
    client_socket, client_address=server_socket.accept()
    with open(file_name, "wb") as file:
      
      while True:
        data=server_socket.recv(1024)
        if not data:
          break
        file.write(data)
      print("finish proccess")  
        

  except ValueError:
    print("didnt find the file")
get_file("newimg.jpg", "127.0.0.1", 8080)    




      
      


