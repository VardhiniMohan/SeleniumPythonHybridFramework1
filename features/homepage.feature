Feature: HomePage functionalities


  Scenario: Register into website successfully
    Given I open the application using URL in browser
    And I navigate to register page
    When I enter mandatory details in register page
    And I click on register button
    Then I should get to login page

  Scenario: Login into website successfully
    Given I open the application using URL in browser
    And I navigate to login page
    When I enter mandatory details in login page
    And I click on login button
    When I enter keys in send keys field
    And I click continue
    Then I should get to account page

  Scenario: Access homepage after login
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should get to home page

  Scenario: Checking home page details
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should get correct website URL and page title in home page

  Scenario: Checking homepage refresh
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    And I click on the logo again
    Then I should get to home Page
