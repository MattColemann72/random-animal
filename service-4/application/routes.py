# from flask import render_template, Response
# import random

from application import app


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def genanimal3():
    #hippopotamus,elephant,monkey,dolphin,zebra
    G2animals = ["Hippo", "Eleph", "Monk", "Dol", "Zeb"]
    G2randAnimal = random.choice(G2animals)
    #lion,dog,cat,cow,sheep
    G1animals = ["on", "og", "at", "ow", "eep"]
    G1randAnimal = random.choice(G1animals)

    service4animal = G1randAnimal + G2randAnimal
    
    return render_template('index.html', title="Random Animal Name Generator", service4animal=service4animal)