import serial


def waitForByte(ser, search: str):
    found = ''
    while(search not in found):
        res = ser.readline()
        try:
            found = res.decode("utf-8")
        except:
            pass

    return found


region = 1


with serial.Serial('/dev/tty.usbserial-0001', 9600, timeout=1) as ser:
    # enter command mode
    ser.write(b'+++')
    print(waitForByte(ser, "OK"))

    # set wireless id
    s = f'ATMY{region // 4 + 1}00{region % 4}\r'
    print(f'Wireless ID (MY): {s}')
    ser.write(str.encode(s))
    print(waitForByte(ser, "OK"))

    # set PAN id
    s = f'ATID{region // 4 + 1}000\r'
    print(f'Pan ID (ID): {s}')
    ser.write(str.encode(s))
    print(waitForByte(ser, "OK"))

    # set dest low
    s = f'ATDL{region // 4 + 1}10{region % 4}\r'
    print(f'Dest Low (DL): {s}')
    ser.write(str.encode(s))
    print(waitForByte(ser, "OK"))

    # set dest high
    ser.write(b'ATDH0000\r')
    print(waitForByte(ser, "OK"))

    # set channel
    ser.write(b'ATCH001A\r')
    print(waitForByte(ser, "OK"))

    # write config
    ser.write(b'ATWR\r')
    print(waitForByte(ser, "OK"))

    # exit command mode
    ser.write(b'ATCN\r')
    print(waitForByte(ser, "OK"))
