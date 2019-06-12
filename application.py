from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit

app=Flask(__name__)

socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('home.html')

@socketio.on('my event')
def handle_my_custom_event(json):
    print(str(json))
    socketio.emit('my response',json)

if __name__=="__main__":
    socketio.run(app, debug=True)
