from flask import render_template, Response
import random

from application import app



@app.route('/', methods = ['GET', 'POST'])
@app.route('/animal1', methods = ['GET', 'POST'])
def genanimal1():

    # Shark, Octopus, Reindeer, Orangutan, Bat
    # Shar, Octop, Reind, Orang, Pi
    G1animals = ["Sha", "Octo", "Rei", "Orangu", "Ba"]

    
    return Response(G1randAnimal, mimetype='text/plain')

