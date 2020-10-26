from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app = Flask(__name__)

todo_list = [
    ("Buy Milk", "adam@gmail.com", "High"),
    ("GO to gym", "daviad123@hotmail.com", "High"),
    ("Cook ", "ray1@gmail.com", "Low")

]


@app.route('/')
def display_list():
    # display
    return render_template('todo.html', todo_list=todo_list)


@app.route('/submit', methods=["POST"])
def submit():
    """
    Processing the data
    """
    global todo_list

    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    todo_list.append((task, email, priority))

    return redirect(url_for('display_list'))


@app.route('/clear')
def clear():
    """
    Clear the list
    """
    global todo_list

    todo_list = []
    return redirect(url_for('display_list'))


@app.route('/delete', methods=['DELETE'])
def delete():
    delete_index = int(request.form['index'])
    del todo_list[delete_index]
    return redirect(url_for('display_list'))

if __name__ == '__main__':
    app.run(debug=True)
