#!/bin/python3
from ast import literal_eval
import socket

class MySocket:
    RECEIVECONDITION = 1024
    MSGLEN = 1024

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        sent = self.sock.send(msg)
        if sent == 0:
            raise RuntimeError("socket connection broken")

    # Return decoded ascii string
    def myreceive(self):
        chunk = self.sock.recv(MySocket.RECEIVECONDITION)
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        return chunk.decode()

    def mysendHardLength(self, msg):
        totalsent = 0
        while totalsent < MySocket.MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceiveHardLength(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MySocket.MSGLEN:
            chunk = self.sock.recv(min(MySocket.MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)

    def myreceive2Suffix(self, suffix):
        """Receive bytes over socket `sock` until we receive the `suffix`."""
        message = self.myreceive()
        if not message:
            raise EOFError('socket closed')
        while not message.endswith(suffix):
            data = self.myreceive()
            if not data:
                raise IOError('received {!r} then socket closed'.format(message))
            message += data
        return message


if __name__ == "__main__":
    # test to umdctf jay 1
    IP = "chals3.umdctf.io"
    PORT = 6002
    SUFFIX = '\n\n'
    addtuple = (IP, PORT)
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client = MySocket(s)
    client.connect(IP, PORT)
    initialMessage = client.myreceive2Suffix(SUFFIX)
    #print("{}\nMessage Length: {}".format(initialMessage, len(initialMessage)))
    response = "\n".encode()
    client.mysend(response)
    arr = client.myreceive2Suffix(SUFFIX)
    #print("Array string length: {}".format(len(arr)))

    matrix = literal_eval(arr)
    print(type(literal_eval(arr)))
    print(matrix)
