from flask import render_template, redirect, url_for, request

from application import app, db
from application.models import Ingredients, Method
from application.forms import IngredientsForm, MethodForm

@app.route('/', methods=[ 'GET', 'POST'])
def index() :
   all_recipes = Recipe.query.all()
   return render_template( 'index.html', all_recipes=all_recipes )
