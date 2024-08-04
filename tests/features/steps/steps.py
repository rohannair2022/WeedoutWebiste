import requests
from behave import *
from bs4 import BeautifulSoup

@given('I visit the site for the first time')
def step_impl(context):
	response = requests.get(context.base_url)
	context.scrapper = BeautifulSoup(response.content, 'html.parser')

@when(u'I want to know more about the product')
def step_impl(context):
	return True

@then(u'I should see a prominent "Github link" on the landing page')
def step_impl(context):
	# 'a' is the tag that the scrapper tries to find
	# lamda creates a function called 'href'
	# the func href then checks if the attribute href exists in a and if it contains 'github.com' 
	context.github_link = context.scrapper.find('a', href=lambda href: href and "github.com" in href)
	if context.github_link is not None:
		return True
	else:
		raise NotImplementedError("Github Link not working")

@then(u'clicking the "Github link" should take me to the "product\'s repository"')
def step_impl(context):
	git_repo = context.github_link['href']
	response = requests.get(git_repo)
	if response.status_code == 200:
		return True 
	else:
		raise Exception("Failed to reach repo")

@then(u'I should see a prominent "LinkedIn link" on the landing page')
def step_impl(context):
	context.linkedin_link = context.scrapper.find('a', href=lambda href: href and "linkedin.com" in href)
	if context.linkedin_link is not None:
		return True
	else:
		raise Exception("Not implemented correctly")

@then(u'clicking the "LinkedIn link" should take me to the "product\'s linkedin site"')
def step_impl(context):
	linkedin_site = context.linkedin_link['href']
	response = requests.get(linkedin_site)
	if response.status_code != 200:
		return True
	else:
		raise Exception("Not being redirected correctly")

@when(u'I want to use the product')
def step_impl(context):
	return True

@then(u'I should see a "product link" that allows me to use the product in question.')
def step_impl(context):
	context.product_link = context.scrapper.find('a', class_="redirect btn btn-outline-light" )
	if context.product_link is not None:
		return True
	else:
		raise Exception("Something wrong with the product link")

@then(u'clicking the "product link" should take me to the page hosting the "products UI"')
def step_impl(context):
    if context.product_link:
        start_button_url = context.product_link['href']
        context.response = requests.get(f"{context.base_url}{start_button_url}")
        if context.response.status_code != 200:
            raise Exception("Failed to be redirected correctly")
    else:
        raise Exception('"Click here to get started" button not found')
