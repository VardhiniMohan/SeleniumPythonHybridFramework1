Feature: Hero section functionality

  Scenario: To validate proper placement of images.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see the image in hero section within viewport

  Scenario: To validate Ui of hero section
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see correct font size and padding

  Scenario: To verify resizing of image in hero section
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should observe resizing of image upon resizing screen

  Scenario: To validate Download and Demo options open appropriate pages
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    And I click Free Download option in hero section
    Then I should get download page
    And I navigate to home page from download page
    And I click view demo option in hero section
    Then I should get demo page



