import time
import math
from threading import Thread, Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room,close_room, rooms, disconnect

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

async_mode = None
if async_mode is None:
    try:
        import eventlet
        async_mode = 'eventlet'
    except ImportError:
        pass

    if async_mode is None:
        try:
            from gevent import monkey
            async_mode = 'gevent'
        except ImportError:
            pass

    if async_mode is None:
        async_mode = 'threading'

    print('async_mode is ' + async_mode)

# monkey patching is necessary because this application uses a background
# thread
if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()

#Start up Flask server:
app = Flask(__name__, template_folder = './',static_url_path='/static')
app.config['SECRET_KEY'] = 'secret!' #shhh don't tell anyone. Is a secret
socketio = SocketIO(app, async_mode = async_mode)
thread = None


def dataThread():
    pass

@app.route('/')
def index():
    global thread
    print ("A user connected")
    if thread is None:
        thread = Thread(target=dataThread)
        thread.daemon = True
        thread.start()
    return render_template('pages/index.html')

# # Autopilot for sliders
# @socketio.on('reporting_1069')
# def action(content):
#     # Define variables
#     unique = content['unique']
#     div = content['div']
#     data = content['data'] 
#     # Emit Variables
#     socketio.emit('autopilot_{}'.format(unique),data=(div,data))
#     # break

# @socketio.on('lit')
# def action():
#     print("It is indeed very, very lit")

if __name__ == '__main__':
    socketio.run(app, port=3000, debug=True)



    