import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server pokrenut...")

conn, addr = server.accept()
print(f"Povezan klijent: {addr}")

while True:
    message = conn.recv(1024).decode()

    if not message:
        break

    print("Primljeno od klijenta:", message)

    with open("client_log.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")

    if message.lower() == "end":
        break

    reversed_message = " ".join(message.split()[::-1])

    print("Poslato klijentu:", reversed_message)
    conn.send(reversed_message.encode())

conn.close()
server.close()