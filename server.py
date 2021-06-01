import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    authorizer = DummyAuthorizer()

    #user login
    authorizer.add_user('root', 'admin123', '.', perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    handler = FTPHandler
    handler.authorizer = authorizer

    #client login
    handler.banner = "pyftpdlib based ftpd ready"
    address = ('127.0.0.1', 2121)
    server = FTPServer(address, handler)

    #limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    #start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()
