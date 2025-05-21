from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import evenlet
from scanner import scan_network

evenlet.monkey_patch()

app = Flask(__name__, static_folder='../frontend', static_url_path='')
socketio = SocketIO(app)


@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@socketio.on('scan')
def handle_scan(data):
    devices = scan_network()
    socketio.emit('scan_result', devices)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0, port=5000')
