

from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()





@app.route('/contact', methods=['POST'])
def contact():

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    conn = sqlite3.connect('users.db')
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name,email,phone,message) VALUES (?,?,?,?)",
        (name,email,phone,message)
    )

    conn.commit()
    conn.close()

    return "Message sent successfully!"




@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Web App Assignment</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            nav a { margin-right: 15px; font-weight: bold; text-decoration: none; }
            nav { margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Home</a>
            <a href="/add">Add User</a>
            <a href="/users">View Users</a>
        </nav>

        <h1>Welcome to the Web App</h1>
        <p>This application stores user information in a database.</p>
    </body>
    </html>
    '''

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()

        return redirect('/users')

    return '''
    <html>
    <head>
        <title>Add User</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            nav a { margin-right: 15px; font-weight: bold; text-decoration: none; }
            nav { margin-bottom: 20px; }
            input { margin-bottom: 10px; padding: 6px; width: 250px; }
            button { padding: 8px 14px; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Home</a>
            <a href="/add">Add User</a>
            <a href="/users">View Users</a>
        </nav>

        <h1>Add User</h1>

        <form method="post">
            <label>Name:</label><br>
            <input name="name" required><br>

            <label>Email:</label><br>
            <input name="email" type="email" required><br>

            <button type="submit">Save User</button>
        </form>
    </body>
    </html>
    '''

@app.route('/users')
def users():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    conn.close()

    html = '''
    <html>
    <head>
        <title>Stored Users</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            nav a { margin-right: 15px; font-weight: bold; text-decoration: none; }
            nav { margin-bottom: 20px; }
            table { border-collapse: collapse; }
            th, td { padding: 8px 12px; border: 1px solid #ccc; }
        </style>
    </head>
    <body>
        <nav>
            <a href="/">Home</a>
            <a href="/add">Add User</a>
            <a href="/users">View Users</a>
        </nav>

        <h1>Stored Users</h1>

        <table>
            <tr><th>ID</th><th>Name</th><th>Email</th></tr>
    '''

    for user in data:
        html += f"<tr><td>{user[0]}</td><td>{user[1]}</td><td>{user[2]}</td></tr>"

    html += '''
        </table>
    </body>
    </html>
    '''

    return html







@app.route('/messages')
def messages():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, phone, message FROM contacts")
    data = cur.fetchall()
    conn.close()

    html = '''
    <html>
    <head>
        <title>Admin Board - Messages</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f9f9f9;
            }
            h1 {
                color: #333;
            }
            table {
                border-collapse: collapse;
                width: 100%;
                background: white;
            }
            th, td {
                border: 1px solid #ccc;
                padding: 12px;
                text-align: left;
                vertical-align: top;
            }
            th {
                background-color: #66BFBF;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            .nav {
                margin-bottom: 20px;
            }
            .nav a {
                text-decoration: none;
                color: #11999E;
                font-weight: bold;
                margin-right: 15px;
            }
        </style>
    </head>
    <body>
        <div class="nav">
            <a href="/">Home</a>
            <a href="/users">Users</a>
            <a href="/messages">Messages</a>
        </div>

        <h1>Contact Messages</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Message</th>
            </tr>
    '''

    for row in data:
        html += f"""
            <tr>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
                <td>{row[2]}</td>
                <td>{row[3]}</td>
                <td>{row[4]}</td>
            </tr>
        """

    html += '''
        </table>
    </body>
    </html>
    '''

    return html




if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)


