# dummy_ticket_api/app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.json
    ticket_id = 'TICKET-1'
    return jsonify({'ticket_id': ticket_id, 'data': data}), 201

@app.route('/tickets/<ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    return jsonify({'ticket_id': ticket_id, 'status': 'open'})

if __name__ == '__main__':
    app.run(port=5001)
