import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Ingredients, Method, Recipe

test_ingredients_name = "peppers"
test_method_steps = "step1. step2, step3"
test_method_time = "50 mins"


test_recipe_name = "paella"
test_recipe_ingredient_id = 1
test_recipe_quantity = "100g"
test_recipe_method_id = 1

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DB_URI')
        app.config['SECRET_KEY'] = getenv('SECRET_KEY')
        return app
    
    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/hlistersims/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

        def tearDown(self):
            self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)


class TestRecipe(TestBase):

    def test_recipes(self):

        self.driver.find_element_by_xpath("/html/body/a[5]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(test_recipe_name)
        self.driver.find_element_by_xpath('//*[@id="ingredient_id"]').send_keys(
            test_recipe_ingredient_id)
        self.driver.find_element_by_xpath('//*[@id="quantity"]').send_keys(
            test_recipe_quantities)
        self.driver.find_element_by_xpath('//*[@id="method_id"]').send_keys(
            test_method_id)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('index') in self.driver.current_url


if __name__ == '__main__':
    unittest.main(port=5000)
