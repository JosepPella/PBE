import board
import serial
from adafruit_pn532.uart import PN532_UART

class Rfid:
    def __init__(self):
        self.uart = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1)
        self.pn532 = PN532_UART(self.uart)

    def read_uid(self):
        self.pn532.SAM_configuration()

        while True:
            uid = self.pn532.read_passive_target(timeout=0.5)
            if uid is not None:
                return ''.join(format(x, '02x') for x in uid)

if __name__ == "__main__":
    rf = Rfid()
    uid = rf.read_uid()
    print(uid)
