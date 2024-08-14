Feature: Loading Landing Page

As a User
I want to be able to be greeted by a landing page when I reach the site
So that I can quickly decide wether the product is something I want to use or not.

Scenario: Github Link on the Landing Page
	Given I visit the site for the first time
	When I want to know more about the product
	Then I should see a prominent "Github link" on the landing page
	And clicking the "Github link" should take me to the "product's repository"

Scenario: LinkedIn Link on the Landing Page
	Given I visit the site for the first time
        When I want to know more about the product
        Then I should see a prominent "LinkedIn link" on the landing page
        And clicking the "LinkedIn link" should take me to the "product's linkedin site"

Scenario: Product Redirect Link on the Landing Page which redirects to the Index Page
	Given I visit the site for the first time 
	When I want to use the product
	Then I should see a "product link" that allows me to use the product in question.
	And clicking the "product link" should take me to the page hosting the "products UI"

 	