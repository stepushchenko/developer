# BEHAVE

BDD - Behavioral Driven Development <br>
Process where tests are written before the actual code <br>
The scripting language used for this format is called Gherkin

Example of BDD for a login page
```html
Feature: Login as a valid user
    Scenario: Login as an existing user
        Given I am a user with a valid credentials
        When I login with my credentials
        Then I should see the text "Welcome" and my full name
```

