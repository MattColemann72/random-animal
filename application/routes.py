from flask import render_template
from application import app
import random



@app.route('/', methods=['POST', 'GET'])
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
        anim1 = "do"
        animal1 = "Dog"
    elif randAnimal1 == 3:
        anim1 = "ca"
        animal1 = "Cat"
    elif randAnimal1 == 4:
        anim1 = "co"
        animal1 = "Cow"
    elif randAnimal1 == 5:
        anim1 = "she"
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