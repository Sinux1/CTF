#!/bin/python3

import socket

from MySocket import MySocket
from MaxSubArray import maxSubArraySum
if __name__ == "__main__":
    IP = "chals3.umdctf.io"
    PORT = 6001
    SUFFIX = '\n\n'

    addtuple = (IP, PORT)
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client = MySocket(s)
    client.connect(IP, PORT)
    initialMessage = client.myreceive2Suffix(SUFFIX)
    print("{}\nMessage : {}".format(initialMessage, len(initialMessage)))
    response = "\n".encode()
    client.mysend(response)
    arr = client.myreceive2Suffix(SUFFIX)
    # Before passing the list along we have to clean the data,
    # becasue it is a string at this point
    print("{}\nArray : {}".format(arr, len(arr)))
    newarr = arr.lstrip("[").rstrip("]\n")
    listRes = list(newarr.split(", "))
    listInts = list(map(int, listRes))
    result = maxSubArraySum(listInts, len(listInts))
    
    response = "{}, {}, {}".format(*result).encode()
    print("Response is: {} ".format(response.decode()))
    client.mysend(response)

    flag = client.myreceive()
    print(flag)
