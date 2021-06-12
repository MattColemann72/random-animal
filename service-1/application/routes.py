from flask import render_template, request, jsonify, json
from sqlalchemy import desc
import requests

from application import app, db
from application.forms import GenerateAnimal
from application.models import AnimalNames

##This is implementation-2

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():

    animal1 = ""
    animal2 = ""

    form = GenerateAnimal()

    if request.method == 'GET':
        return render_template('index.html', title="Random Animal Name Generator", form=form)
    
    if form.validate_on_submit():
        userlanding = False
        get_animal1 = requests.get('http://service-2:5000/animal1').text
        animal1 = get_animal1
        get_animal2 = requests.get('http://service-3:5000/animal2').text
        animal2 = get_animal2
        makeanimalname = requests.post('http://service-4:5000/animal3', json={"anim1":animal1, "anim2":animal2 })

        newanimal = makeanimalname.text


        # Shark,    Octopus,    Reindeer,   Orangutan,  Pig
        # Shar,     Octop,      Reind,      Orang,      Pi
        if animal1 == "Shark":
            animal1 = "Shar"
        if animal1 == "Octopus":
            animal1 = "Octop"
        if animal1 == "Reindeer":
            animal1 = "Reind"
        if animal1 == "Orangutan":
            animal1 = "Orang"
        if animal1 == "Pig":
            animal1 = "Pi"

        # Giraffe,  Lizzard,    Rhino,  Flamingo,   Penguin
        # raffe,     zard,        hino,    mingo,       guin 
        if animal2 == "Giraffe":
            animal2 = "raffe"
        elif animal2 == "Lizzard":
            animal2 = "zard"
        elif animal2 == "Rhino":
            animal2 = "hino"
        elif animal2 == "Flamingo":
            animal2 = "mingo"
        elif animal2 == "Penguin":
            animal2 = "guin"

        
        db.session.add(AnimalNames(animalname = newanimal))
        db.session.commit()

        allanimalnames = AnimalNames.query.order_by(desc(AnimalNames.id)).limit(5).all()

        return render_template('index.html', title="Random Animal Name Generator", userlanding=userlanding, newanimal=newanimal, allanimalnames=allanimalnames, animal1=animal1, animal2=animal2, form=form)#randanimal=randanimal, animal2=animal2, animal1=animal1, form=form, )
