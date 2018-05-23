import serial
from serial.tools import list_ports
from serial.serialutil import SerialException
import time

class Dongle:
    def __init__(self, debug=False):
        self.debug = debug
        PORT = self.find_microbit()
        BAUD = 115200
        self.connect(PORT, BAUD)
    
    def log(self, msg):
        if self.debug:
            print(msg)

    def find_microbit(self):
        microbit = None
        self.log("Searching for a microbit")
        while microbit is None:
            ports = list(list_ports.comports())
            for p in ports:
                if (p.pid == 516) and (p.vid == 3368):
                    microbit = str(p.device)
            self.log("No microbit found :(")
            self.log("Trying again...\n")
            time.sleep(0.5)
        self.log("Found a microbit at %s" % microbit)
        return microbit

    def connect(self, port, baud):
        connected = False
        while connected is False:
            try:
                s = serial.Serial(port)
                s.baudrate = baud
                s.parity = serial.PARITY_NONE
                s.databits = serial.EIGHTBITS
                s.stopbits = serial.STOPBITS_ONE
            except SerialException:
                self.log("Microbit is busy. Trying again...")
                time.sleep(2)
            else:
                connected = True
        self.s = s
        self.log("Connected to microbit successfully")

    def recv(self):
        data = self.s.readline().decode("UTF-8").rstrip()
        return data

    def send(self, data):
        self.s.write(data.encode())

    def sendd(self, data):
        for line in data.split("\n"):
            self.send(line+"\r")
