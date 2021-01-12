# coding: utf-8

"""
Source : 
Date : 05/01/2021
Auteur : Christian Doriath
Dossier : /Python34/MesDEv/Flask/FlaskBootstrap_BASE
Fichier : app.py
Description : app flask de base pour utiliser Bootstrap 4.0

Mot cles : 
"""

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def myindex():
    return render_template('index.html')

# @app.route('/test0')
# def mytest0():
#     return render_template('test0.html')

# @app.route('/test1')
# def mytest1():
#     return render_template('test1.html')
