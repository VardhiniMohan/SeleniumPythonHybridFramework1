Feature: Footer functionality

  Scenario: To validate options under Opencart in footer.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see Opencart options in footer
    And I click on Features option under opencart
    Then I should get features page
    And I click on Showcase option under opencart
    Then I should get Resource-showcase page
    And I click on Demo option under opencart
    Then I should get demo page
    And I click on Download option under opencart
    Then I should get download page
    And I click on Marketplace option under opencart
    Then I should get marketplace page
    And I click on Login option under opencart
    Then I should get to Account page

  Scenario: To validate options under Company in footer.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see Company options in footer
    And I click on Contact Us option under Company
    Then I should get Contact page
    And I click on Extension Advertising option under Company
    Then I should get Advertising page
    And I click on Marketplace Advertising option under Company
    Then I should get Advertising page
    And I click on About Us option under Company
    Then I should get Company page
    And I click on Terms & Conditions option under Company
    Then I should get Policy page
    And I click on Extension Developer option under Company
    Then I should get Extension Developer page

  Scenario: To validate options under Support in footer.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see Support options in footer
    And I click on Community Forum option under Support
    Then I should get Community forum page
    And I click on Dedicated Support option under Support
    Then I should get Support page
    And I click on OpenCart Partners option under Support
    Then I should get Resources-Partners page
    And I click on Marketplace Support option under Support
    Then I should get Support page
    And I click on Migrate to OpenCart option under Support
    Then I should get Migrate to OpenCart page

  Scenario: To validate options under Resources in footer.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see resources options in footer
    And I click on OpenCart Blog option under Support
    Then I should get blog page
    And I click on OpenCart Documentation option under Support
    Then I should get resource-Documentation page
    And I click on OpenCart Books option under Support
    Then I should get resource-Books page
    And I click on GitHub Bug Tracker option under Support
    Then I should get resource-GitHub Bug Tracker page
    And I click on Developer option under Support
    Then I should get resource-developer page

  Scenario: To validate the options under Newsletter option in the footer.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should see Newsletter section in footer
    Then I should see Newsletter statement under Newsletter
    Then I should see correct placeholder text in input field

  Scenario: To validate the Social media links.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Given I save this as parent window
    Then I should see Social section in footer
    And I click on Facebook Marketing Partner option under Social
    Then I should get Meta-partners page
    And I click on LinkedIn option under Social
    Then I should get LinkedIn page
    And I click on Facebook option under Social
    Then I should get Facebook page
    And I click on Twitter option under Social
    Then I should get Twitter page

  Scenario: To validate "Sign-up for Newsletter" form.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    And I enter email in newsletter input field
    And I click on arrow
    Then I should see "Sign-up for Newsletter" form pop-up

  Scenario: To validate the UI of the footer.
    Given I open the application using URL in browser
    And I navigate to login page
    And I successfully login into the application
    When I click on the logo
    Then I should observe correct padding, margin, font size and line height in content section





