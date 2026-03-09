# Setup Instructions (Run the Project Locally)

Follow these steps to run the application on your local machine.

1. Clone the Repository

Download the project from GitHub.

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git

Then move into the project directory:

cd webapp


2. Install Python

Make sure Python 3 is installed.

Check by running:

python3 --version

If Python is not installed, download it from:
https://www.python.org/downloads/


3. Install Required Dependencies

Install Flask using pip:

pip3 install flask

If the project includes a requirements.txt file, run:

pip3 install -r requirements.txt


4. Create the Database

Run SQLite to create the database file:

sqlite3 users.db

Create the contacts table:

CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    message TEXT
);

Exit SQLite:

.exit


5. Start the Flask Server

Run the Flask application:

python3 app.py

You should see something like:

Running on http://127.0.0.1:5000


6. Open the Application

Open a browser and visit:

http://localhost:5000


7. Test the Contact Form

Fill out the contact form and submit a message.

The message will be stored in the SQLite database.


8. View Submitted Messages

Open the admin dashboard:

http://localhost:5000/messages

This page displays all stored contact messages.


9. View Submitted Messages from the Terminal

You can view stored contact form messages directly from the server using SQLite.

First, navigate to the project directory:

cd webapp

Then open the database:

sqlite3 users.db

Once inside SQLite, run the following command to display all stored messages:

SELECT * FROM contacts;

Example output:

1|John Doe|john@email.com|5551234567|Hello, I am interested in your work
2|Jane Smith|jane@email.com|5559876543|Please contact me about a project

Each column represents:

ID | Name | Email | Phone | Message

To exit SQLite, run:

.exit


Troubleshooting

If the server does not start, make sure:

• Python 3 is installed  
• Flask is installed  
• You are inside the project directory  
• The database file exists  

You can recreate the database if needed.
