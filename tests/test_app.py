import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Ingredients, Method, Recipe

class TestBase( TestCase ):
    def create_app(self):

        app.config.update( SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):

        db.create_all()

        ingedient1 = Ingredients(name="Milk")
        method1 = Method(steps="hello", time="40mins")

        db.session.add(sample1) 
        db.session.add(method1)
        db.session.commit()
        recipe1= Recipe(name="recipe", ingredient_id=sample1.id, quantity="100g", method_id=method1.id)

        db.session.add(recipe1)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()


class TestViews( TestBase ):

    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', recipe_id=1) )
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', recipe_id=1))
        self.assertEqual(response.status_code, 302)

    def test_addIn_get(self):
        response = self.client.get(url_for('addIn'))
        self.assertEqual(response.status_code, 200)

    def test_ingredients_get(self):
        response = self.client.get(url_for('ingredients'))
        self.assertEqual(response.status_code, 200)

    

class TestAdd( TestBase ) :
    def test_add_ingredient(self):
        response = self.client.post(
            url_for('addIn'),
            data = dict(name="Eggs")
        )
        self.assertIn(b'Eggs', response.data)

    def test_add_methods(self):
        response = self.client.post(
            url_for('methods', method_id=1),
            data = dict(steps="step 1", time="1 hour"),
            follow_redirects=True
        )
        self.assertIn(b'step 1', response.data)
        self.assertIn(b'1 hour', response.data)

    def test_add_recipe(self):
        response = self.client.post(
            url_for('recipes'),
            data = dict(name="Chilli Con Carne", ingredient_id=2, quantity="500g", method_id=2),
            follow_redirects=True
            )
        self.assertIn(b'Chilli Con Carne', response.data)
        self.assertIn(b'2', response.data)
        self.assertIn(b'500g', response.data)
        self.assertIn(b'2', response.data)
    
    def test_addIn_not_valid(self):
        response = self.client.post(
            url_for('addIn'),
            data = dict(name="13/11/2020"),
            follow_redirects=True
            )
        self.assertEqual(response.status_code, 405)


class TestUpdate( TestBase ):
    def test_update_recipe(self):
        response = self.client.post(
            url_for('update', recipe_id=1),
            data = dict(oldname="Lasagne", newname="Lasagne serves 42"),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)

class TestDelete( TestBase ) :
    def test_delete_recipe(self):
        response = self.client.post(
            url_for('delete', recipe_id=1),
            data = dict(name="Pasta"),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,405)
