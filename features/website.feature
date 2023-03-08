Feature: Website functionality

  Scenario: Open website with URL
    Given I open the application using URL in browser
    Then I should get website homepage

  Scenario: Open website in different browsers
    Given I Open the application using URL in browser
    Then I should get website homepage
    And I close the driver
    Given I Open the application using URL in edge browser
    Then I should get website homepage

  Scenario: Check working of website
    Given I Open the application using URL in browser
    And I click on feature option
    Then I should get features page