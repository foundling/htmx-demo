from collections import OrderedDict

from flask import Flask, render_template, request
from flask_cors import CORS 


app = Flask(__name__) 
CORS(app)


def todo_maker(todo_id=None):

    if todo_id is None:
        todo_id = 1

    def make_todo(title, todo_id=0):
        todo_id += 1
        
        return {
            'title': title,
            'id': str(todo_id)
        }

    return make_todo



make_todo = todo_maker()

todos = {}

todo = make_todo('learn htmx')
todos[todo['id']] = todo 

@app.route('/todo', methods=['POST'])
def create_todo():

    todo = request.form.get('todo')
    if todo:
        todo_id = len(todos) + 1
        todos[todo_id] = make_todo(title=todo)

    return render_template('todos.html', todos=todos)
# how to reconcile dict structure in templates?
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todos', methods=['GET'])
def get_todos():
    return render_template('todos.html', todos=todos)

@app.route('/todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):

    if todos.get('id'):
        del todos['id']


    return render_template('todos.html', todos=todos)
