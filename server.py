from ast import And
from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'Super_Secret_Key'

@app.route('/')
def index():
    if 'intentos' in session:
        session['intentos'] += 1

    if 'random_number' not in session:
        session['random_number'] = random.randint(1, 100)

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess_num'] = int(request.form['random_number'])

    if 'intentos' not in session:
        session['intentos'] = 0
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)