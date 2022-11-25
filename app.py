from passlib.hash import argon2
from flask import Flask, request, render_template
import sqlite3
import db_create
app = Flask(__name__)


@app.route('/authorization', methods=['GET', 'POST'])
def form_authorization():
    if request.method == 'POST':
        Username = request.form.get('Username')
        Password = request.form.get('Password')

        db_lp = sqlite3.connect('username_password.db')
        cursor_db = db_lp.cursor()
        cursor_db.execute(('''SELECT password FROM passwords
                                               WHERE username = '{}';
                                               ''').format(Username))
        pas = cursor_db.fetchall()

        cursor_db.close()
        try:
            if argon2.verify(Password, pas[0][0]) == False:
                return render_template('authorization_failed.html')
        except:
            return render_template('authorization_failed.html')

        db_lp.close()
        return render_template('authorization_success.html')

    return render_template('authorization.html')


@app.route('/registration', methods=['GET', 'POST'])
def form_registration():

    if request.method == 'POST':
        Username = request.form.get('Username')
        Password = request.form.get('Password')
        Password_hash = argon2.hash(Password)
        db_lp = sqlite3.connect('username_password.db')
        cursor_db = db_lp.cursor()
        sql_insert = '''INSERT INTO passwords VALUES('{}','{}');'''.format(
            Username, Password_hash)

        cursor_db.execute(sql_insert)

        cursor_db.close()

        db_lp.commit()
        db_lp.close()

        return render_template('registration_success.html')

    return render_template('registration.html')


@app.route('/logout')
def logout():
    return render_template('authorization.html')


if __name__ == "__main__":
    app.run()
