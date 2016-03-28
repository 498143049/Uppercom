# coding=UTF-8
# it can simulate serial to send datas it uses python 
# 2016 03 28 
from time import sleep, ctime
import serial
import threading
port='com3';
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
   		Myserial.write(str.encode('ascii'));
   		sleep(2)
   except KeyboardInterrupt :
   	Myserial.close()
   	print ("Off ")

   	