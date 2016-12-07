from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('network.html', title='Главная')

@app.route('/data/', methods=['POST'])
def data():
    name=request.form['start']
    pasw=request.form['finish']
    return render_template('data.html', name=name, pasw=pasw, title='Данные')