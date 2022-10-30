from digi.xbee.devices import XBeeDevice
import time


def main():
    # Instantiate a local XBee object.
    xbee = XBeeDevice("COM6", 9600)
    try:
        xbee.open()
    except Exception as e:
        print(e)
        print("COM port does not exist or is invalid")
        return

    for _ in range(100):
        xbee.send_data_broadcast("Hello XBee World!")
        time.sleep(.1)

    xbee.close()


if __name__ == '__main__':
    main()
