# ChatRoom
Chat Room with admin account

## Install library 

```
pip install threading
pip install socket
```

## Run server

Run `server.py` on 
```
host = '127.0.0.1'
port = 55556
```

## Server is running 

![image](https://user-images.githubusercontent.com/76879087/120870168-814dea00-c598-11eb-94ba-443d402f0293.png)

## Client 

Connect to sevrer by client 

First step is run `client.py`

![image](https://user-images.githubusercontent.com/76879087/120870377-1355f280-c599-11eb-9f58-02fa0d36c8ae.png)

On server see who connect with server 

![image](https://user-images.githubusercontent.com/76879087/120870404-29fc4980-c599-11eb-9787-1a5878dee934.png)

So write some 

![image](https://user-images.githubusercontent.com/76879087/120870578-92e3c180-c599-11eb-84bd-b0b904ce1b94.png)

We will see the message in a way `user: hi`

## Admin command 

Kick command on `server2.py`

``` python 
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
            else:
                broadcast(message)

def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send('You are kicked by admin'.encode('ascii'))
        client_to_kick.close()
        nicknames.remove(name)
        broadcast(f'{name} was kicked by admin'.encode('ascii'))
```

Kick command on `client2.py`

```python 
def write():
    while True:
        if stop_thread:
            break
        message = f'{nickname}: {input("")}'
        if message[len(nickname)+2:].startswith('/'):
            if nickname == 'admin':
                if message[len(nickname)+2:].startswith('/kick'):
                    client.send(f'KICK {message[len(nickname)+2+6:]}'.encode('ascii'))
                elif message[len(nickname)+2:].startswith('/ban'):
                    client.send(f'BAN {message[len(nickname)+2+5:]}'.encode('ascii'))
            else:
                print("Commands can only executed by the admin")
        else:
            client.send(message.encode('ascii'))
```

# Login to admin 

![image](https://user-images.githubusercontent.com/76879087/120871390-c7587d00-c59b-11eb-896b-c22506a308cf.png)

If you write wrong password code is break

# Kick on admin 

![image](https://user-images.githubusercontent.com/76879087/120871503-13a3bd00-c59c-11eb-9b33-2ade08fc93b5.png)


# TO DO 

- [ ] add on hosting 
- [ ] GUI
