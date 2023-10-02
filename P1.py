import board
import busio
from adafruit_pn532.i2c import PN532_I2C

class Rfid:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.pn532 = PN532_I2C(i2c, address=0x24)
        self.pn532.SAM_configuration()

    def read_uid(self):
        while True:
            uid = self.pn532.read_passive_target()
            if uid is not None:
                return ''.join(format(x, '02x') for x in uid)

if __name__ == "__main__":
    rf = Rfid()
    uid = rf.read_uid()
    print(uid)
