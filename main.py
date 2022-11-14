import socket
import traceback
import sys
import pyperclip as pc
from PIL import ImageGrab
import numpy as np
import traceback

class ServerConnection:
    def __init__(self):
        self.running = True
        self.sock = socket.socket()
        self.prevCopy = self.GetValue()
        self.port = 8080
        self.MemoryBuffer = 1024
        self.NotifyPort()
        self.name = socket.gethostname()
        self.connectionName = self.EstablishHostName()
        self.AttemptConnection()
        self.Run()

    def Run(self):
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
