import socket
import pyperclip as pc
from PIL import ImageGrab
import numpy as np

def GetValue():
    ping = pc.paste()
    if not ping:
        ping = ImageGrab.grabclipboard().convert("RGB")
    return ping

def arrayToString(array):
    for i in range(len(array)):
        for i2 in range(len(array[i])):
            array[i][i2] = "SUB3".join(array[i][i2])
        array[i] = "SUB2".join(array[i])
    array = "SUB1".join(array)
    return array

s = socket.socket()
prevCopy = ""
name = socket.gethostname()
print(name)

host = "SION-LAPTOP"

port = 8080

s.connect((host, port))


while True:
    ping = GetValue()
    if prevCopy != ping:
        if type(ping) == str:
            input_ = "STRING FORMAT - " + ping
            input_ = input_.encode("utf-8")
        else:
            array = np.array(ping)
            array = array.astype(str)
            array = arrayToString(array.tolist())
            input_ = array.encode("utf-8")
        s.send(input_)
        prevCopy = ping
