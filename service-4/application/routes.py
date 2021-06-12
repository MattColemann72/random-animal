from flask import request, Response
# import random

from application import app


@app.route('/', methods = ['GET', 'POST'])
@app.route('/animal3', methods = ['GET', 'POST'])
def makeanimnames():
    animslist = request.data.decode('utf-8')
    anim1 = request.json["anim1"]
    anim2 = request.json["anim2"]
    newanimname = anim1+anim2
    
    return Response(newanimname, mimetype='text/plain')