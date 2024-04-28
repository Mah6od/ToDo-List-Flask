from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

tasks = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append({'name': task, 'done': False})
    return render_template('todos.html', title="Get It Done!", tasks=tasks)

@app.route('/toggle_done/<int:task_index>', methods=['POST'])
def toggle_done(task_index):
    if request.method == 'POST':
        if 0 <= task_index < len(tasks):
            task = tasks[task_index]
            task['done'] = not task['done']
    return redirect('/')

app.run()