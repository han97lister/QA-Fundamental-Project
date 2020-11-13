from flask import render_template, redirect, url_for, request

from application import app, db
from application.models import Ingredients, Method, Recipe
from application.forms import IngredientsForm, MethodForm, RecipeForm

@app.route('/', methods=[ 'GET', 'POST'])
def index() :
   all_recipes = Recipe.query.all()
   return render_template( 'index.html', all_recipes=all_recipes )

@app.route('/ingredients', methods=['GET', 'POST'])
def ingredients() :
    all_ingredients = Ingredients.query.all()
    return render_template('ingredients.html', all_ingredients=all_ingredients)

@app.route('/addIn', methods=['GET', 'POST'])
def addIn() :
    form = IngredientsForm()
    if form.validate_on_submit() :
        ingredient = Ingredients(
             name = form.name.data
        )
        db.session.add(ingredient)
        db.session.commit()
        return redirect( url_for('ingredients') )
    return render_template('addIn.html', title="Add an Ingredient", form=form)

@app.route('/method', methods=['GET', 'POST'])
def methods() :
    form = MethodForm()
    if form.validate_on_submit() :
        methods = Method(
            steps = form.steps.data,
            time = form.time.data
            )
        db.session.add(methods)
        db.session.commit()
        return redirect( url_for('new_method') )
    return render_template( 'methods.html', title="Add a Method", form=form)

@app.route('/new_method', methods=['GET', 'POST'])
def new_method() :
    new_method = Method.query.all()
    return render_template('new_method.html', new_method=new_method)

@app.route('/recipe', methods=['GET', 'POST'])
def recipes() :
    form = RecipeForm()
    
    ingredients=Ingredients.query.all()
    choices =[]
    for ingredient in ingredients :
        choices.append((ingredient.id, ingredient.name))
    form.ingredient_id.choices=choices

    methods=Method.query.all()
    choices=[]
    for method in methods :
        choices.append((method.id, method.steps))
    form.method_id.choices=choices

    if form.validate_on_submit() :
        recipes = Recipe(
            name = form.name.data,
            ingredient_id = form.ingredient_id.data,
            quantity = form.quantity.data,
            method_id = form.method_id.data
            )
        db.session.add(recipes)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('recipe.html', form=form)

@app.route('/update/<int:recipe_id>', methods=['GET', 'POST'])
def update(recipe_id):
    form = RecipeForm()
    recipe_update = Recipe.query.get(recipe_id)
    
    ingredients=Ingredients.query.all()
    choices =[]
    for ingredient in ingredients :
        choices.append((ingredient.id, ingredient.name))
    form.ingredient_id.choices=choices

    methods=Method.query.all()
    choices=[]
    for method in methods :
        choices.append((method.id, method.steps))
    form.method_id.choices=choices

    if form.validate_on_submit() :
        recipe_update.name = form.name.data
        recipe_update.ingredient_id = form.ingredient_id.data
        recipe_update.quantity = form.quantity.data
        recipe_update.method_id = form.method_id.data
        db.session.add(recipe_update)
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.name.data = recipe_update.name
    return render_template('update.html', title = "Update your recipe", form=form)

@app.route('/delete/<int:recipe_id>')
def delete(recipe_id):
    recipe_delete = Recipe.query.get(recipe_id)
    db.session.delete(recipe_delete)
    db.session.commit()
    return redirect(url_for('index'))
