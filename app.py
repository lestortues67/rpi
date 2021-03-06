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

@app.route('/claire')
def myclaire():
    return render_template('claire.html')

@app.route('/papa')
def mypapa():
    return render_template('papa.html')
