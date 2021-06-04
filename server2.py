import threading
import socket

host = '127.0.0.1' #local host
port = 55556

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            msg = message = client.recv(1024)
            if msg.decode('ascii').startswith('KICK'):
                if nicknames[clients.index(client)] == 'admin':
                    name_to_kick = msg.decode('ascii')[5:]
                    kick_user(name_to_kick)
                else:
                    client.send('Command was refused!'.encode('ascii'))


                    'in development'
            #elif msg.decode('ascii').startswith('BAN'):
                #if nicknames[clients.index(client)] == 'admin':
                    #name_to_ban = msg.decode('ascii')[4:]
                    #kick_user(name_to_ban)
                    #with open('bans.txt', 'a') as f:
                        #f.write(f'{name_to_ban}\n')
                    #print(f'{name_to_ban} was banned!')
                #else:
                    #client.send('Command was refused!'.encode('ascii'))


            else:
                broadcast(message)
        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} left!'.encode('ascii'))
                nicknames.remove(nickname)
                break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')

        if nickname == 'admin':
            client.send('PASS'.encode('ascii'))
            password = client.recv(1024).decode('ascii')

            if password != 'admin123':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined!".encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send('You are kicked by admin'.encode('ascii'))
        client_to_kick.close()
        nicknames.remove(name)
        broadcast(f'{name} was kicked by admin'.encode('ascii'))

'''
def ban_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_ban = clients[name_index]
        clients.remove(client_to_ban)
        client_to_ban.send('You are banned by admin'.encode('ascii'))
        client_to_ban.close()
        nicknames.remove(name)
        broadcast(f'{name} was banned by admin'.encode('ascii'))
'''


print("Server is listening...")
receive()

