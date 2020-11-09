from application import db

class Ingredients( db.Model ) :
    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String(30), nullable = False )
    quantity = db.Column( db.String(30), nullable = False )
    recipe = db.relationship('Recipe', backref='ingredients')

class Method( db.Model ) :
    id = db.Column( db.Integer, primary_key = True )
    steps = db.Column( db.String(30), nullable = False )
    time = db.Column( db.Float )
    recipe = db.relationship( 'Recipe', backref='method')

class Recipe( db.Model ) :
    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String(30), nullable = False )
    ingredient_id = db.Column('ingredients_id', db.Integer, db.ForeignKey('ingredients_id'))
    method_id = db.Column('method_id', db.Integer, db.ForeignKey('method_id'))
