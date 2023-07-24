from flask import Flask, render_template, request
from data import connect_db
from datetime import datetime


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    database, cursor = connect_db()

    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        note = request.form['note']

        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert the data into the database
        cursor.execute('INSERT INTO users (name, note, date) VALUES (?, ?, ?)', (name, note, date))
        database.commit()

    # Retrieve the last 10 notes from the database
    cursor.execute('SELECT * FROM users ORDER BY id DESC LIMIT 10')
    notes = cursor.fetchall()

    return render_template('notes.html', notes=notes)


if __name__ == "__main__":
    app.run(debug=True)

