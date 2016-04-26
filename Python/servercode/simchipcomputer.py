# coding=UTF-8
from time import sleep, ctime
import serial
import threading
import random
port='com4';
baudrate=9600;
Myserial = serial.Serial(port,baudrate); 
def Handle(Text124):
	while True:
		count = Myserial.inWaiting()  
		if count != 0:
			recv = Myserial.read(count)
			print(recv.decode('ascii'))
			Myserial.flushInput()
		sleep(0.1)
if __name__ == '__main__':

   str='$ABADCDHB&'
   th=threading.Thread(target = Handle, args=('sda',) )
   th.setDaemon(True)  #主线程退出，子线程也退出
   th.start()

   try:
   	while(True):
   		Myserial.write(bytes([random.randint(0, 255)]));
   		sleep(0.1)
   except KeyboardInterrupt :
   	Myserial.close()
   	print ("Off ")