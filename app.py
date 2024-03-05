import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def yourDummyDB():
    init()
    conn = sqlite3.connect('goods.db')
    c = conn.cursor()
    c.execute('SELECT * FROM goods')
    data = c.fetchall()
    conn.close()
    return render_template('index.html', data=data)

def init():
    conn = sqlite3.connect('goods.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS goods")
    c.execute('''CREATE TABLE goods
                     (id INTEGER PRIMARY KEY, name text, description text, price real, image_path text)''')
    c.execute(
        "INSERT INTO goods (name, description, price, image_path) VALUES ('Chicken Nuggets', 'Delicious chicken nuggets', 35.14, 'static/images/Burger.jpg')")
    c.execute(
        "INSERT INTO goods (name, description, price, image_path) VALUES ('Coca Cola', 'Wonderfull Softdrink', 5.14, 'static/images/Coke.jpg')")
    conn.commit()
    c.execute(
        "INSERT INTO goods (name, description, price, image_path) VALUES ('Chicken Nuggets', 'Crunchy Nuggets', 25.14, 'static/images/Nuggets.jpg')")
    conn.commit()
    c.execute('SELECT * FROM goods')
    print(c.fetchall())
    conn.close()

@app.route('/all')
def display_all():
    conn = sqlite3.connect('goods.db')
    c = conn.cursor()
    c.execute('SELECT * FROM goods')
    data = c.fetchall()
    conn.close()
    return str(data)

@app.route('/goods/<int:id>')
def get_goods_by_id(id):
    conn = sqlite3.connect('goods.db')
    c = conn.cursor()
    c.execute('SELECT * FROM goods WHERE id=?', (id,))
    data = c.fetchone()
    conn.close()
    if data is None:
        return "No data found for ID: " + str(id), 404
    else:
        return render_template('index.html', data=[data])


if __name__ == '__main__':
    app.run()
