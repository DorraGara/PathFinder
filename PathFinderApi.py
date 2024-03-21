from flask import Flask, request, jsonify
from pathfinder import find_path
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def server_up():
    return 'Server is up and running'

@app.route('/find_path', methods=['POST'])
def handle_find_path():
    data = request.json
    initial_position = data.get('initial_position')
    destination_position = data.get('destination_position')

    if initial_position is None or destination_position is None:
        return jsonify({'error': 'Both initial_position and destination_position are required'}), 400

    start = (initial_position.get('x'), initial_position.get('y'))
    end = (destination_position.get('x'), destination_position.get('y'))


    if start is None or end is None:
        return jsonify({'error': 'Both start and end positions are required'}), 400

    path = find_path(start, end)
    return jsonify({'path': path})

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=5000))
