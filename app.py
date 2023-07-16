from flask import Flask, render_template, redirect, request, url_for
from jinja2 import Template
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('todo.db')
cur = conn.cursor()

@app.route("/") 
def welcome():
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()
    cur.execute(" SELECT * FROM todo ")
    c = cur.fetchall()
    x = []
    for i in c:
        (n,) = i
        x.append(n)
    return render_template("index.html", elements = x)

@app.route("/variable", methods=["POST"])
def variab():
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()
    data = request.form.get('data')
    cur.execute(" INSERT INTO todo VALUES (?) ", (data,))
    conn.commit()
    cur.execute(" SELECT * FROM todo ")
    c = cur.fetchall()
    x = []
    for i in c:
        (n,) = i
        x.append(n)
    return render_template("index.html", elements = x)

@app.route("/delete", methods=['POST'])
def dell():
    conn = sqlite3.connect('todo.db')
    cur = conn.cursor()
    data = request.form.get('data')
    cur.execute(" DELETE FROM todo WHERE task = (?)", (data,))
    conn.commit()
    cur.execute(" SELECT * FROM todo ")
    c = cur.fetchall()
    x = []
    for i in c:
        (n,) = i
        x.append(n)
    return render_template("index.html", elements = x)


if __name__ == "__main__":
    app.run(debug=True)