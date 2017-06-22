from flask import Flask, request, session, render_template, redirect, flash
import random
from datetime import datetime


app = Flask(__name__, static_url_path="/static", static_folder="static")
app.secret_key = 'soMuchSecret'


@app.route('/')
def home():
    if 'color' not in session:
        session['color'] = " "
    if 'msg' not in session:
        session['msg'] = []
    if 'current' not in session:
        session['current'] = 0
    if int(session['current']) < 0:
        session['current'] = 0
        # flash 'ouch'

    return render_template('index.html', yourGold=session['current'], msg=session['msg'], color=session['color'])


@app.route('/process_money', methods=['POST', 'GET'])
def money():

    if request.form['where'] == 'farm':
        session['modifier'] = random.randint(9, 20)
        session['current'] += session['modifier']

    elif request.form['where'] == 'cave':
        session['modifier'] = random.randint(5, 10)
        session['current'] += session['modifier']

    elif request.form['where'] == 'house':
        session['modifier'] = random.randint(1, 5)
        session['current'] += session['modifier']

    elif request.form['where'] == 'casino':
        session['modifier'] = random.randint(-50, 50)
        session['current'] += session['modifier']

    session['timestamp'] = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')

    if session['modifier'] < 0:
        session['color'] = 'red'
        session['msg'].append('Entered a casino and lost ' + str(abs(session['modifier'])) + ' golds... Ouch ' + ' (' + str(session['timestamp']) + ')')
    else:
        session['color'] = 'green'
        session['msg'].append('Earned ' + str(session['modifier']) + ' from the ' + request.form['where'] + ' (' + str(session['timestamp']) + ')')
    return redirect('/')


@app.route('/reset')
def reset():
    session.pop('msg')
    session.pop('current')
    session.pop('modifier')
    return redirect('/')
app.run(debug=True)
