from digi.xbee.devices import XBeeDevice
import time


def main():
    # Instantiate a local XBee object.
    xbee = XBeeDevice("/dev/tty.usbserial-0001", 9600)
    try:
        xbee.open()
    except Exception as e:
        print(e)
        print("COM port does not exist or is invalid")
        return

    data = [0xFF] + [0xAA] * 12
    while(True):

        xbee.send_data_broadcast(bytes(data))
        print(f"Sending Data Packet {data}")
        time.sleep(.1)

    xbee.close()


if __name__ == '__main__':
    main()
