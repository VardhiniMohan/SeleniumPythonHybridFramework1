Feature: Page header functionality

  Scenario: To validate all 6 options are displayed in header.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see all 6 options in header

  Scenario: To validate Account and Logout options are displayed in header.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see account and logout options in header

  Scenario: To validate working of all 6 options
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    And I click on feature option
    Then I should get features page
    And I click on demo option
    Then I should get demo page
    And I click on marketplace option
    Then I should get marketplace page
    And I click on blog option
    Then I should get blog page
    And I click on download option
    Then I should get download page
    And I click on resource-developer option
    Then I should get resource-developer page

  Scenario:  To validate working of Account and Logout options
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    And I click on Account option
    Then I should get to Account page
    And I click on logout option
    Then I should get to logout page

  Scenario: To validate UI of Header
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should observe correct UI details in entire header area
    Then I should observe correct UI details in logo area
