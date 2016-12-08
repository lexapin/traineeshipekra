#<<<<<<< HEAD
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def form():
    return render_template('network.html', title='Главная')

#=======
#-*- coding: utf-8 -*-
#>>>>>>> 09d619a2cc987d0aa000da8c705dded02a645714