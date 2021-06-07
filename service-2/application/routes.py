from flask import render_template, Response
import random

from application import app



@app.route('/', methods = ['GET', 'POST'])
@app.route('/animal1', methods = ['GET', 'POST'])
def genanimal1():
    #lion,dog,cat,cow,sheep
    G1animals = ["Li", "Do", "Ca", "Co", "She"]
    G1randAnimal = random.choice(G1animals)
    
    return Response(G1randAnimal, mimetype='text/plain')