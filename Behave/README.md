# BEHAVE

### Применение
- Тестирование WEB-app с Selenium и Selenoid
- Тестирование API со всеми плюсами BDD
- Тестирование SQL со всеми плюсами BDD

### Links to documentation

- Behave https://behave.readthedocs.io/en/stable/tutorial.html
- Environmental controls (code to run before and after steps, scenarios, features or the whole shooting match). https://behave.readthedocs.io/en/stable/tutorial.html#environmental-controls

### BDD Introduction

BDD - Behavioral Driven Development <br>
Process where tests are written before the actual code <br>
The scripting language used for this format is called Gherkin <br>
Bahave (Python) == Cucumber (Ruby)

### BDD commands
- FEATURE
  - SCENARIO
    - GIVEN
    - WHEN
    - THEN
    - BUT
    - AND

### Project directories and files:
- feature_1.feature (file)
- feature_2.featire (file)
- steps (directory)
  - **steps.py** (file)
- features_group_one (directory)
  - feature_3.feature (file)
  - feature_4.feature (file)
  - features_subgroup_one (directory)
    - feature_5.feature (file)
    - feature_6.feature (file)

### Behave test-case example

Feature file
```html
Feature: Logging in with valid credentials
    Scenario: User login successfully
        Given I create a new user
        When I type email
        When I type password
        When I click on Login button
        Then I should see the text Wellcome
```

Steps file
```python
from behave import given, when, then

@when("I type password")
def type_the_pass(context):
    pass

@then("I should see the text Wellcome")
def wellcome(context):
    pass
```

### Run tests

Run all tests
```bash
behave
```

Run a specific scenario
```bash
behave -n "scenario name"
```
