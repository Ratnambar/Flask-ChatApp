from flask import Flask,render_template
from flask_socketio import SocketIO
app = Flask(__name__)
app.config['SECRET_KEY']='secret'
socketio = SocketIO(app)


@app.route("/")
def hello():
    return render_template("chat.html")

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received something:'+str(json))
    socketio.emit('my response',json)



if __name__ == '__main__':
    socketio.run(app,debug=True)