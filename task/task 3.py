from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with a random secret key
socketio = SocketIO(app)


messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@socketio.on('message')
def handle_message(data):
    message = data['message']
    messages.append(message)
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
