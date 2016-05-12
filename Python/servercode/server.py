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
			print("%d,%d,%d"%(recv[0],recv[1],len(recv)));
			socketio.emit('news',{'data': recv[0]/50});
			Myserial.flushInput()
		

@app.route('/')
def index():
    global Myserial
    if Myserial==None:
        Myserial = serial.Serial('com3',9600); #全局
        print ("open")
        th1=threading.Thread(target=BackRead)
        th1.setDaemon(True) 
        th1.start()
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
  socketio.run(app,host='0.0.0.0',port=80);
  print ("Off ")
  # th1=threading.Thread(target = socketio.run, args = (app,) ,kwargs = {'debug':'true','host':'0.0.0.0', 'port':5000})
  # th1.setDaemon(True) 
  # th1.start()
  # thread1 = threading.Thread(target=BackRead)
  # thread1.setDaemon(1)
  # thread1.start()
  # socketio.run(app,debug=True)
  # try:
  #   # while True:
  #   #   time.sleep(0.1);
  #   #   pass
  #   while True:
  #       if Myserial!=None:
  #           count = Myserial.inWaiting();
  #           if count != 0:
  #               recv = Myserial.read(count);
  #               if recv[1]==(recv[0]+1) and recv[2]==(recv[0]-1) :
  #                   print("%d,%d,%d,%d"%(recv[0],recv[1],recv[2],len(recv)));
  #                   Myserial.flushInput();
  #                   socketio.emit('news',{'data':recv[0]*5/255.0});
  #       else:
  #           print ("None")
  #       time.sleep(0.04);

  # except KeyboardInterrupt:
  # 	Myserial.close()
  # 	print ("Off ")
  # threaded参数是为了并发访问 

