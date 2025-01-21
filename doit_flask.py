from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

TODO_FILE = 'todo.json'

# Load tasks from the JSON file
def load_todo():
    if not os.path.exists(TODO_FILE):
        return {}
    with open(TODO_FILE, 'r') as file:
        return json.load(file)

# Save tasks to the JSON file
def save_todo(data):
    with open(TODO_FILE, 'w') as file:
        json.dump(data, file)

# Route to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_todo()
    return jsonify(list(tasks.values()))

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    data = load_todo()
    new_task = request.json.get('task')

    if new_task:
        task_id = str(len(data))
        data[task_id] = new_task
        save_todo(data)
        return jsonify({'message': 'Task added successfully'}), 201
    else:
        return jsonify({'error': 'Invalid task'}), 400

# Route to remove a task by index
@app.route('/remove/<int:index>', methods=['DELETE'])
def remove_task(index):
    data = load_todo()
    task_keys = list(data.keys())

    if 0 <= index < len(task_keys):
        task_id = task_keys[index]
        del data[task_id]
        save_todo(data)
        return jsonify({'message': 'Task removed successfully'}), 200
    else:
        return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
