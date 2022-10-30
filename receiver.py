from digi.xbee.devices import XBeeDevice


def main():
    # Instantiate a local XBee object.
    xbee = XBeeDevice("/dev/tty.usbserial-0001", 9600)
    try:
        xbee.open()

        def data_receive_callback(xbee_message):
            print("From %s >> %s" % (xbee_message.remote_device.get_64bit_addr(),
                                     xbee_message.data.decode()))

        xbee.add_data_received_callback(data_receive_callback)
        print("Waiting for data...\n")
        print("Hit enter to end program")
        input()
    except Exception as e:
        print(e)
        print("COM port does not exist or is invalid")
        return

    xbee.close()


if __name__ == '__main__':
    main()
