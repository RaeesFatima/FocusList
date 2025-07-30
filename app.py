from flask import Flask, request, redirect, url_for
from flask import render_template

app = Flask(__name__)

tasks=[]

@app.route('/')
def hello_world():
    return render_template('index.html',tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    description = request.form.get('description')
    category = request.form.get('category')
    deadline = request.form.get('deadline')
    if title:
        tasks.append({
            'title': title,
            'description': description or '',
            'category': category or '',
            'deadline': deadline or ''
        })
    return redirect(url_for('hello_world'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    tasks.pop(task_id)
    return redirect(url_for('hello_world'))

# @app.route('/edit/<int:task_id>',methods=['POST'])
# def edit(task_id):
#     task=request.form.get('task')
#     if task:
#         tasks[task_id]['task']=task
#     return redirect(url_for('hello_world'))

if __name__=='__main__':
    app.run()
