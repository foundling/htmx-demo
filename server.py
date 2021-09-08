from flask import Flask, render_template, request
from flask_cors import CORS 
from todo import Todo

app = Flask(__name__) 
CORS(app)

todos = {}
#todo = Todo('learn htmx')
#todos[todo.id] = todo 

@app.route('/todo', methods=['POST'])
def create_todo():

    text = request.form.get('text')
    if text:
        todo = Todo(text)
        todos[str(todo.id)] = todo 
    print('POST: ', todos)

    return render_template('todos.html', todos=todos)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
def get_todos():
    return render_template('todos.html', todos=todos)

@app.route('/todo/<string:id>', methods=['DELETE'])
def delete_todo(id):

    print('DELETE. todos: ', todos)
    print('id:', id, 'type: ', type(id))
    if todos.get(id):
        del todos[id]

    print('todos for template re-render: ', todos)
    return render_template('todos.html', todos=todos)
