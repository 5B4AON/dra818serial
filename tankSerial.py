
import time
import serial

ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

try:
    pass
    #ser.open()

except Exception as e:
    print("error opening serial port: " + str(e))
    exit()

if ser.isOpen():

    try:
        ser.flushInput() #flush input buffer, discarding all its contents
        ser.flushOutput()#flush output buffer, aborting current output

        serialcmd = "AT+DMOCONNECT\r\n"
        ser.write(serialcmd.encode())
        time.sleep(0.5)
        numberOfLine = 0

        while True:

            response = ser.readline()
            print("read data: " + str(response.decode()))

            numberOfLine = numberOfLine + 1
            if (numberOfLine >= 5):
                break

        ser.close()

    except Exception as e:
        print("error communicating...: " + str(e))

else:
    print("cannot open serial port ")
