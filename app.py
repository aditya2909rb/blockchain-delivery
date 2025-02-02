from flask import Flask, request
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    socketio.emit('location_update', data)
    return {'status': 'success'}, 200

@app.route('/update_delivery_status', methods=['POST'])
def update_delivery_status():
    data = request.json
    socketio.emit('delivery_status_update', data)
    return {'status': 'success'}, 200

if __name__ == '__main__':
    socketio.run(app, debug=True)
