import socket
import threading 

HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER, PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def newurl(msg):
	status="ALREADY HTTPS 200"
	new_msg=msg
	if msg[4]!='s':
		new_msg="https"+msg[4:]
		status="REDIRECTED SUCCESFULLY 302"	
	return new_msg, status
	
def handle_client(conn,addr):
	print(f"[NEW CONNECTION] {addr} connected")
	connected=True
	while connected:
		msg_length=conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length=int(msg_length)
			msg=conn.recv(msg_length).decode(FORMAT)
			if msg==DISCONNECT_MESSAGE:
				connected=False
			new_msg, status=newurl(msg)
			print(new_msg)
			print(status)
	#conn.close()

def start():
	server.listen()
	print(f"[LISTENING] server is listenening on {SERVER} ")
	while True:
		conn, addr= server.accept()
		thread =threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

print("[STARTING] server is starting.. ")
start()
