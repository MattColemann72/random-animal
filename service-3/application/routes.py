from flask import render_template, Response
import random

from application import app


@app.route('/', methods = ['GET', 'POST'])
@app.route('/animal2', methods = ['GET', 'POST'])
def genanimal2():
    # Giraffe, Lizzard, Rhino, Flamingo, Penguin, Armadillo
    # raffe, zard, hino, mingo, guin
    G2animals = ["raffe", "zard", "hino", "mingo", "guin", "dillo"]
    G2randAnimal = random.choice(G2animals)
    
    return Response(G2randAnimal, mimetype='text/plain')

