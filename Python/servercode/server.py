from flask import Flask,render_template
from flask_socketio import SocketIO  #增加socket IO

import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')



@app.route('/')
def index():
   return app.send_static_file('user.html')
@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

if __name__ == '__main__':
  socketio.run(app)  
  # threaded参数是为了并发访问 

