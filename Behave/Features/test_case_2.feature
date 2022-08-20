Feature: Attempt to login in with invalid credentials

  Scenario: None existing user try to login
    Given I generate a random email address
    When I type random email
    When I type password
    When I click on Login
    Then I should see the text Error: user not found

  Scenario: User try to login with wrong password
    Given I create a user
    When I type correct email
    When I type random password
    When I click on Login
    Then I should see the text Error: incorrect password

  Scenario: User try to login with no password
    Given I create a new user
    When I type correct email
    When I click on Login
    Then I should see the text Error: password field is empty