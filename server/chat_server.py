import socket
import threading
from crypto_helper import encrypt_message, decrypt_message
from control_logic import execute_command

host = '0.0.0.0'  # 監聽所有IP
port = 12345

server = socket.socket()
server.bind((host, port))
server.listen(1)
print("🔒 安全聊天室伺服器已啟動，等待連線...")

client, addr = server.accept()
print(f"📞 使用者來自 {addr} 已連線")

def receive():
    while True:
        try:
            data = client.recv(4096)
            if not data:
                print("⚠️ 客戶端已離線")
                break
            decrypted = decrypt_message(data.decode())
            if decrypted.lower() == 'exit':
                print("👋 對方離開了聊天室")
                break
            print(f"\n對方說：{decrypted}")
            execute_command(decrypted)
        except Exception as e:
            print("⚠️ 接收錯誤：", e)
            break

def send():
    while True:
        try:
            msg = input("你說：")
            encrypted = encrypt_message(msg)
            client.send(encrypted.encode())
            if msg.lower() == 'exit':
                print("你離開了聊天室。")
                client.close()
                break
        except:
            break

recv_thread = threading.Thread(target=receive, daemon=True)
send_thread = threading.Thread(target=send)

recv_thread.start()
send_thread.start()

send_thread.join()

