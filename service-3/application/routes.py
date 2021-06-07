from flask import render_template, Response
import random

from application import app


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def genanimal2():
    #hippopotamus,elephant,monkey,dolphin,zebra
    G2animals = ["potamus", "phant", "key", "phin", "bra"]
    G2randAnimal = random.choice(G2animals)
    
    return Response(G2randAnimal, mimetype='text/plain')