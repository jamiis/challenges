from __future__ import print_function
from select import select

import socket, sys, argparse

SIZE = 1024

def parse_data(data):
    return data.split('|')

def serve(handler, port):
    # host = socket.gethostbyname(socket.gethostname())
    host = 'localhost'
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((host, port))
        print("listening on {0}:{1}".format(host, port))
    except socket.error, msg:
        print("Error binding the server socket. "
            "Code: {0}, Message:{1}".format(*msg))
        sys.exit(1)

    server.listen(0)

    inputs = [server]
    outputs = []
    while inputs:
        readable, writable, exceptional = select(inputs,outputs,inputs)
        for s in readable:
            if s is server:
                # requesting a connection
                connection, client_address = s.accept()
                connection.setblocking(0)
                inputs.append(connection)
            else:
                # an established connection is sending data
                data = s.recv(SIZE)
                if not data: break
                # extract message type and data from packet
                msg_type, msg_data = parse_data(data)
                # close connection
                if msg_type == 'GoodBye':
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
                else:
                    handler(msg_type, msg_data)

        # TODO handle outputs
        # for s in writable

        # TODO handle exceptions
        # for s in exceptional

    server.close()

if __name__ == "__main__":
    # parse commandline arguments
    parser = argparse.ArgumentParser(description='Start TCP message server')
    parser.add_argument('--port', 
        type=int, 
        help='Bind server to port (default: 4242)',
        default=4242,
    )
    handlers = {
        'print': print
    }
    parser.add_argument('--handler', 
        help='Message processing function (default: print)',
        default='print',
    )
    cmdargs = parser.parse_args()

    # start server
    serve(
        handlers[cmdargs.handler],
        cmdargs.port
    )
