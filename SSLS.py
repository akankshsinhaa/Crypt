import socket
import ssl

# Generate SSL context
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('localhost', 10000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

# Wrap the socket with SSL
secure_socket = context.wrap_socket(server_socket, server_side=True)

print("Server is listening...")

try:
    while True:
        # Wait for a connection
        connection, client_address = secure_socket.accept()
        
        try:
            print(f"Connection from {client_address}")
            
            # Receive the data from client
            data = connection.recv(1024)
            if data:
                print(f"Received: {data.decode('utf-8')}")
                # Echo back to client
                connection.sendall(data)
            else:
                break
            
        finally:
            # Clean up the connection
            connection.close()
            
finally:
    # Clean up the socket
    secure_socket.close()
