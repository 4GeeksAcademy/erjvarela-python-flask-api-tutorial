from flask import Flask, jsonify, request

todos =[ { "label": "My first task", "done": False } ]

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    json_data = jsonify(todos)
    return json_data

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    response = jsonify(todos)
    return response

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    response = jsonify(todos)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
