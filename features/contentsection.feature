Feature: Content section functionality

  Scenario: To validate UI of content section
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should observe correct font size and line height in content section

  Scenario: To validate the resizing of home page contents when screen is resized.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should observe resizing of contents upon resizing screen

  Scenario: To validate links in section 2 of content section
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Given I save this as parent window
    Then I should see section 2 in content section
    And I click on british red cross logo
    Then I should get british red cross website
    And I click on BJPenn logo
    Then I should get BJPenn website
    And I click on Concordia College logo
    Then I should get Concordia College website
    And I click on FX Creations logo
    Then I should get FX Creations website
    And I click on HKU logo
    Then I should get HKU website

  Scenario: To validate presence of section 3 and marketplace option
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see section 3 in content section
    And I click on Visit Marketplace option in section 3
    Then I should get marketplace page

  Scenario: To validate presence of section 4 and visit all option
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see section 4 in content section
    And I click on Visit All option in section 3
    Then I should get marketplace page

  Scenario: To validate presence of section 5
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see section 5 in content section
    Then I should see correct padding and text alignment

  Scenario: To validate section 6 and its options
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see section 6 in content section
    And I click on Community support- learn more option
    Then I should get Community forum page
    And I click on Dedicated support- learn more option
    Then I should get Dedicated support page

  Scenario: To validate section 7 and its options
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Given I save this as parent window
    Then I should see section 7 in content section
    And I click on Forbes logo
    Then I should get forbes page
    And I click on Paypal logo
    Then I should get paypal page
    And I click on BBC logo
    Then I should get BBC page
    And I click on South China Morning Post logo
    Then I should get South China Morning Post  page








