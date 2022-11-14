import socket
import traceback
import sys
import pyperclip as pc
import random
from PIL import ImageGrab
import numpy as np
import traceback

class ServerConnection:
    def __init__(self):
        self.running = True
        self.hostSock = socket.socket()
        self.sock = socket.socket()
        self.prevCopy = self.GetValue()
        self.port = 0
        self.hostPort = random.randint(1000, 7500)
        self.MemoryBuffer = 1024
        self.name = socket.gethostname()
        self.NotifyName()
        self.NotifyPort()
        self.createServer()
        self.connectionName = self.EstablishHostName()
        self.AttemptConnection()
        self.Run()

    def createServer(self):
        self.hostSock.bind((self.name, self.hostPort))
        self.hostSock.listen(1)
    def NotifyName(self):
        print("Your Device's Name is: " + self.name)
    def Run(self):
        print("The device is now connected and running")
        while self.running:
            NewValue = self.GetValue()
            if NewValue != self.prevCopy:
                self.SendInput(NewValue)
                self.prevCopy = NewValue

    def SendInput(self, String):
        chunks = []
        chunkInput = ""
        for letter in String:
            size = sys.getsizeof(chunkInput)
            if size >= 7 * self.MemoryBuffer / 8:
                chunks.append(chunkInput)
                chunkInput = ""
            else:
                chunkInput += letter
        chunks = [str(len(chunks))] + chunks
        for buffer in chunks:
            print(buffer)
            self.sock.send(buffer.encode("utf-8"))

    def LB(self):
        print('\033[95m' + "-" * 50 + '\033[0m')

    def AttemptConnection(self):
        self.LB()
        self.sock.connect((self.connectionName, self.port))
        print("Connection established with %s." % self.connectionName)

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
        print("Your port is %d" % self.hostPort)
        print("Please input the port displayed on the device you are connecting to.")
        self.port = int(input("Device port: "))

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
