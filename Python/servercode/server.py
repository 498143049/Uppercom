from flask import Flask,render_template
from flask_socketio import SocketIO  #增加socket IO
import time
import threading
from threading import Timer
from threading import Thread
import eventlet
import random
import serial
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')
thread = None;
Myserial= None;
def timer():
	while True:
		time.sleep(0.1)
		print("I am doing ");
		socketio.emit('news',{'data': random.random()*2});
def BackRead():
	global Myserial
	print("I am Raad");
	while True:
		time.sleep(0.1)
		count = Myserial.inWaiting()  
		if count != 0:
			recv = Myserial.read(count)
			print("%d,%d"%(recv[0],len(recv)));
			Myserial.flushInput()
		

@app.route('/')
def index():
   return app.send_static_file('starter.html')
@socketio.on('my event')
def handle_my_custom_event(json):
	pass
	# global thread
	# if thread is None:
	# 	thread = Thread(target=timer);
	# 	thread.daemon = True;
	# 	thread.start();
	# print('I am starting')
    # print('received json:'+str(json));
if __name__ == '__main__':

  th1=threading.Thread(target = socketio.run, args = (app,) ,kwargs = {'debug':'true'})
  th1.setDaemon(True) 
  th1.start()
  Myserial = serial.Serial('com5',9600); #全局
  # thread1 = threading.Thread(target=BackRead)
  # thread1.setDaemon(1)
  # thread1.start()
  # socketio.run(app,debug=True)
  try:
  	while True:
  		count = Myserial.inWaiting()  
  		if count != 0:
  			recv = Myserial.read(count)
  			print("%d,%d"%(recv[0],len(recv)));
  			Myserial.flushInput()
  			socketio.emit('news',{'data':recv[0]/100.0});
  		time.sleep(0.05)
  except KeyboardInterrupt:
  	Myserial.close()
  	print ("Off ")
  # threaded参数是为了并发访问 

