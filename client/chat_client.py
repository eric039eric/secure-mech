import socket
import threading
from crypto_helper import encrypt_message, decrypt_message

host = "192.168.XXX.XXX" #記得切換成你的server端Ipv4位址
port = 12345

s = socket.socket()
s.connect((host, port))

def receive():
    while True:
        try:
            data = s.recv(4096)
            if not data:
                print ("對方已離線")
                break
            decrypted = decrypt_message(data.decode())
            print (f"\n對方說:{decrypted}")
        except Exception as e:
            print ("接收錯誤", e)
            break
def send():
    while True:
        msg = input("你說")
        encrypted = encrypt_message(msg)

        if isinstance(encrypted, str):
            s.send(encrypted.encode())
        else:
            s.send(encrypted)

        if msg.lower() == 'exit':
            print ("你已離開聊天室。")
            s.close()
            break

recv_thread = threading.Thread(target=receive, daemon=True)
send_thread = threading.Thread(target=send)

recv_thread.start()
send_thread.start()

send_thread.join()