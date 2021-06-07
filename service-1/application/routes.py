from flask import render_template, request, jsonify, json
from sqlalchemy import desc
import random, requests

from application import app
from application.forms import GenerateAnimal



@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():

    animal1 = ""
    animal2 = ""
    randanimal = ""

    # animal1 = "Lion"
    # animal2 = "dog"
    # animal3 = "cat" 
    # animal4 = "cow"
    # animal5 = "sheep"
    # animal6 = "hippopotamus"
    # animal7 = "Elephant" 
    # animal8 = "Monkey"
    # animal9 = "Dolphin"
    # animal10 = "Zebra"

    form = GenerateAnimal()


    if request.method == 'GET':
        return render_template('index.html', title="Random Animal Name Generator", form=form)
    
    if form.validate_on_submit():
        get_animal1 = requests.get('http://service-2:5001/animal1')
        animal1 = get_animal1.text
        get_animal2 = requests.get('http://service-3:5002/animal2')
        animal2 = get_animal2.text

        randanimal = animal1 + animal2

    return render_template('index.html', title="Random Animal Name Generator", randanimal=randanimal, animal2=animal2, animal1=animal1, form=form)
