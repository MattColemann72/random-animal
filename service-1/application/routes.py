from flask import render_template
from application import app
from application.forms import GenerateAnimal
import random



@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def index():
    randAnimal1 = random.randint(1,5)
    randAnimal2 = random.randint(6,10)
    animal1 = ""
    animal2 = ""
    anim1 = ""
    anim2 = ""
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

    if randAnimal1 == 1:
        anim1 = "Li"
        animal1 = "Lion"
    elif randAnimal1 == 2:
        anim1 = "Do"
        animal1 = "Dog"
    elif randAnimal1 == 3:
        anim1 = "Ca"
        animal1 = "Cat"
    elif randAnimal1 == 4:
        anim1 = "Co"
        animal1 = "Cow"
    elif randAnimal1 == 5:
        anim1 = "She"
        animal1 = "Sheep"
    
    if randAnimal2 == 6:
        anim2 = "potamus"
        animal2 = "Hippopotamus"
    elif randAnimal2 == 7:
        anim2 = "phant"
        animal2 = "Elephant"
    elif randAnimal2 == 8:
        anim2 = "key"
        animal2 = "Monkey"
    elif randAnimal2 == 9:
        anim2 = "phin"
        animal2 = "Dolphin"
    elif randAnimal2 == 10:
        anim2 = "bra"
        animal2 = "Zebra"

    randanimal = anim1 + anim2

    # print(randanimal)

    return render_template('index.html', title="Random Animal Name Generator", randanimal=randanimal, animal2=animal2, animal1=animal1)


# from flask import render_template, request, url_for, Response, jsonify, json
# from application import app, db
# from application.forms import GenerateForm
# from application.models import characters
# from sqlalchemy import desc
# import random, requests, time


# @app.route('/', methods = ['GET', 'POST'])
# @app.route('/home', methods = ['GET', 'POST'])
# def home():
#     form = GenerateForm()
#     if request.method == 'GET':
#         return render_template('home.html', title='Class', form=form)
#     if form.validate_on_submit():
#         get_class = requests.get('http://service_two:5001/class')
#         character_class = get_class.text
#         get_race = requests.get('http://service_three:5002/race')
#         character_race = get_race.text
#         name = requests.post('http://service_four:5003/name', data=character_race)
#         character_name = name.text
#         stat = requests.post('http://service_four:5003/stats', data=character_race)
#         stat_dict = json.loads(stat.text)
#         data = characters(
#                 name = character_name,
#                 char_class = character_class,
#                 char_race = character_race)
#         db.session.add(data)
#         db.session.commit()
        
#         stored_characters = characters.query.order_by(desc(characters.id)).limit(5).all()

#         return render_template('home.html', title='Class', form=form, classes=character_class, race=character_race, name=character_name, stats=stat_dict, all_characters=stored_characters)
