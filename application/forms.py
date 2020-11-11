from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, TimeField
from wtforms.validators import DataRequired, ValidationError

from application.models import Ingredients, Method, Recipe

class IngredientsForm( FlaskForm ) :
    name = StringField( 'Ingredient',
        validators = [
            DataRequired()
        ]
    )
    submit = SubmitField( 'Add ingredient' )

class MethodForm( FlaskForm ) :
    steps = TextAreaField( 'Method',
        validators = [
            DataRequired()
        ]
    )
    time = TimeField( 'Estimated time', format='%H:%M' )
    submit = SubmitField( 'Add Method' )

#class RecipeForm( FlaskForm ) :

