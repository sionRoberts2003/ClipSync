import socket
import traceback

import pyperclip as pc
from PIL import ImageGrab
import numpy as np
import traceback

class ServerConnection:
    def __init__(self):
        self.running = True
        self.sock = socket.socket()
        self.prevCopy = self.GetValue()
        self.name = socket.gethostname()
        self.connectionName = self.EstablishHostName()
        self.port = 8080
        self.NotifyPort()
        self.AttemptConnection()

    def Run(self):
        while self.running:
            pass

    def LB(self):
        print('\033[95m' + "-" * 50 + '\033[0m')

    def AttemptConnection(self):
        self.LB()
        try:
            self.sock.connect((self.name, self.port))
            print("Connection established with %s." % self.name)
        except:
            print('\033[91m' + "Connection between host name is not found." + '\033[0m')
            self.RetryConnection()

    def RetryConnection(self):
        self.LB()
        print("Would you like to try another device name?")
        response = input("y/n: ")
        if response == "y":
            self.EstablishHostName()
            self.AttemptConnection()
        else:
            quit()

    def NotifyPort(self):
        print("Your port is %d" % self.port)

    def EstablishHostName(self):
        self.LB()
        print("Input the host name of the other computer you are trying to connect to.")
        print("This is labeled as the host name on your other device.")
        return input("Client Name: ")

    def GetValue(self):
        ping = pc.paste()
        if not ping:
            ping = ImageGrab.grabclipboard().convert("RGB")
        return ping

if __name__ == "__main__":
    server = ServerConnection()
