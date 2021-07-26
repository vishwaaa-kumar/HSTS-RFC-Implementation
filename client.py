import socket

HEADER=64
PORT=5050
FORMAT='utf-8'
SERVER=socket.gethostbyname(socket.gethostname())
DISCONNECT_MESSAGE="!DISCONNECT"
ADDR=(SERVER,PORT)

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
	message=msg.encode(FORMAT)
	msg_length=len(message)
	send_length=str(msg_length).encode(FORMAT)
	send_length+= b' '*(HEADER-len(send_length))
	client.send(send_length)
	client.send(message)
	
requested= ["https://www.google.com",
			"https://www.youtube.com",
			"https://www.mail.google.com",
			"https://www.netflix.com",
			"https://www.web.whatsapp.com",
			"https://www.microsoft.com",
			"https://www.teams.microsoft.com",
			"https://www.reddit.com",
			"https://www.discord.com",
			"https://www.wikipedia.com",
			"https://www.annauniv.edu",
			"https://www.amazon.com",
			"https://www.facebook.com",
			"https://www.instagram.com",
			"https://epgp.inflibnet.ac.in"]


def check(url):
	flag=0
	if url[4]!='s':
		url="https"+url[4:]
	for x in requested:
		if x==url:
			flag=1
			#print(f"{x} {flag}")
	return flag, url

i=0
while i<2:
	flag=0
	url=input("Enter the url: ")
	actual_url=url
	flag, url=check(url)
	if flag==0:
		#print(f"{flag}")
		requested.append(url)
		send(actual_url)
	if flag==1:
		#print(f"{flag}")
		send(url)
	print("The client side web browser has cached the following URLs ")
	for y in requested:
		print(f"{y}")
	i=i+1
