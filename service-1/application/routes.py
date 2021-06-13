from flask import render_template, request, jsonify, json
from sqlalchemy import desc
import requests

from application import app, db
from application.forms import GenerateAnimal
from application.models import AnimalNames



@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():

    animal1 = ""
    animal2 = ""

    form = GenerateAnimal()

    # if request.method == 'GET':
    #     return render_template('index.html', title="Random Animal Name Generator", form=form)
    
    if form.validate_on_submit():
        userlanding = False
        get_animal1 = requests.get('http://service-2:5000/animal1').text
        animal1 = get_animal1
        get_animal2 = requests.get('http://service-3:5000/animal2').text
        animal2 = get_animal2
        makeanimalname = requests.post('http://service-4:5000/animal3', json={"anim1":animal1, "anim2":animal2 })

        newanimal = makeanimalname.text
    else:
        get_animal1 = requests.get('http://service-2:5000/animal1').text
        animal1 = get_animal1
        get_animal2 = requests.get('http://service-3:5000/animal2').text
        animal2 = get_animal2
        makeanimalname = requests.post('http://service-4:5000/animal3', json={"anim1":animal1, "anim2":animal2 })

        newanimal = makeanimalname.text



        #Lion,  Dog,    Cat,    Cow,    Sheep
        #"Li",  "Do",   "Ca",   "Co",   "She"
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
        if animal2 == "phant":
            animal2 = "Elephant"
        if animal2 == "key":
            animal2 = "Monkey"
        if animal2 == "phin":
            animal2 = "Dolphin"
        if animal2 == "bra":
            animal2 = "Zebra"
        
        db.session.add(AnimalNames(animalname = newanimal))
        db.session.commit()

        allanimalnames = AnimalNames.query.order_by(desc(AnimalNames.id)).limit(5).all()

        return render_template('index.html', title="Random Animal Name Generator", userlanding=userlanding, newanimal=newanimal, allanimalnames=allanimalnames, animal1=animal1, animal2=animal2, form=form)#randanimal=randanimal, animal2=animal2, animal1=animal1, form=form, )
