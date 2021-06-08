from flask import render_template, request, jsonify, json
from sqlalchemy import desc
import requests

from application import app
from application.forms import GenerateAnimal



@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():

    animal1 = "animal 1"
    animal2 = "animal 2"
    randanimal = "new animal"

    form = GenerateAnimal()

    if request.method == 'GET':
        return render_template('index.html', title="Random Animal Name Generator", form=form)
    
    if form.validate_on_submit():
        get_animal1 = requests.get('http://service-2:5000/animal1').text
        animal1 = get_animal1.text
        get_animal2 = requests.get('http://service-3:5000/animal2').text
        animal2 = get_animal2.text

        randanimal = animal1 + animal2
        #Lion, Dog, Cat, Cow, Sheep
        #"Li", "Do", "Ca", "Co", "She"
        if animal1 == "Li":
            animal1 = "Lion"
        elif animal1 == "Do":
            animal1 = "Dog"
        elif animal1 == "Ca":
            animal1 = "Cat"
        elif animal1 == "Co":
            animal1 = "Cow"
        elif animal1 == "She":
            animal1 = "Sheep"
        
        #hippopotamus,elephant,monkey,dolphin,zebra
        # "potamus", "phant", "key", "phin", "bra"
        if animal2 == "potamus":
            animal2 = "Hippopotamus"
        elif animal2 == "phant":
            anima2 = "Elephant"
        elif animal2 == "key":
            anima2 = "Monkey"
        elif animal2 == "phin":
            anima2 = "Dolphin"
        elif animal2 == "bra":
            anima2 = "Zebra"

            

        return render_template('index.html', title="Random Animal Name Generator", randanimal=randanimal, animal2=animal2, animal1=animal1, form=form)

        

    return render_template('index.html', title="Random Animal Name Generator", randanimal=randanimal, animal2=animal2, animal1=animal1, form=form)