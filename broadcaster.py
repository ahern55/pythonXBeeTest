import time
import serial


def main():

    with serial.Serial('/dev/tty.usbserial-0001', 9600, timeout=1) as ser:
        data = [0xFF] + [0x69] * 12
        while(True):
            ser.write(bytes(data))
            print(f"Sending Data Packet {data}")
            time.sleep(.1)


if __name__ == '__main__':
    main()
