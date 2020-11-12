from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.models import Ingredients, Method, Recipe

class IngredientsForm( FlaskForm ) :
    name = StringField( 'Ingredient',
        validators = [
            DataRequired()
        ]
    )
    submit = SubmitField( 'Add ingredient' )

class MethodForm( FlaskForm ) :
    steps = TextAreaField( 'Steps',
        validators = [
            DataRequired()
        ]
    )
    time = StringField( 'Estimated time' )
    submit = SubmitField( 'Add Method' )
    
class RecipeForm( FlaskForm ) :
    name = StringField( 'Name',
        validators = [
            DataRequired()
        ]
    )
    ingredient_id = SelectField('Choose Ingredients', choices=[])
    quantity = StringField( 'Enter the quantities',
        validators = [
            DataRequired()
        ]
    )
    method_id = SelectField('Choose Method', choices=[])
    submit = SubmitField( 'Complete Recipe' )

