import serial
port = serial.Serial("/dev/ttyUSB0", baudrate = 9600, bytesize = 8, stopbits = 1, timeout = 2)
port.open()

for i in range(0, 500):
	port.write("#250 0 250 0 250 0 250 0!")
	
print "%d" % i
data = port.read(30)
print data
port.close()
print"""Good
Bye"""
