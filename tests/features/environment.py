# environment.py

from os import getenv
from selenium import webdriver

WAIT_SECONDS = int(getenv('WAIT_SECONDS', '60'))
BASE_URL = getenv('BASE_URL', 'http://127.0.0.1:5001/')

def before_all(context):
    """ Executed once before all tests """
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    context.driver = webdriver.Firefox(options=options)
    context.driver.implicitly_wait(context.wait_seconds)

def after_all(context):
    """ Executed after all tests """
    context.driver.quit()
