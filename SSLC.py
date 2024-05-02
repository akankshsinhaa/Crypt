import socket
import ssl

# Generate SSL context
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(cafile="server.crt")

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL
secure_socket = context.wrap_socket(client_socket, server_hostname='localhost')

# Connect to the server
server_address = ('localhost', 10000)
secure_socket.connect(server_address)

try:
    # Send data to server
    message = "Hello, Server!"
    print(f"Sending: {message}")
    secure_socket.sendall(message.encode('utf-8'))
    
    # Receive data from server
    data = secure_socket.recv(1024)
    print(f"Received: {data.decode('utf-8')}")
    
finally:
    # Clean up the socket
    secure_socket.close()
