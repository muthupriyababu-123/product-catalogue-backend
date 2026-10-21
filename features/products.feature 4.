
Feature: Product catalogue management

  Background:
    Given the following products
      | name    | description       | category | available | price |
      | Hat     | A red fedora      | Clothing | true      | 12.00 |
      | Shoes   | Running shoes     | Clothing | false     | 45.00 |
      | Big Mac | Burger            | Food     | true      | 5.00  |
      | Sheets  | Cotton bed sheets | Home     | true      | 20.00 |

  Scenario: Read a product
    Given I am on the "Home Page"
    When I enter "Hat" in the "Name" field
    And I click the "Search" button
    Then I should see the product "Hat"
    When I copy the ID of product "Hat"
    And I clear the form
    And I enter the copied ID in the "Product ID" field
    And I click the "View" button
    Then I should see the message "Success"
    And I should see "Hat" in the product details

  Scenario: Update a product
    Given I am on the "Home Page"
    When I search for product "Hat"
    And I copy the ID of product "Hat"
    And I clear the form
    And I enter the copied ID in the "Product ID" field
    And I click the "View" button
    And I click the "Edit" button
    And I enter "Updated Hat" in the "Name" field
    And I click the "Update" button
    Then I should see the message "Product updated successfully"

  Scenario: Delete a product
    Given I am on the "Home Page"
    When I search for product "Hat"
    And I copy the ID of product "Hat"
    And I clear the form
    And I enter the copied ID in the "Product ID" field
    And I click the "View" button
    And I click the "Delete" button
    Then I should see the message "Product has been Deleted!"

  Scenario: List all products
    Given I am on the "Home Page"
    When I clear the form
    And I click the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    And I should see "Shoes" in the results
    And I should see "Big Mac" in the results
    And I should see "Sheets" in the results

  Scenario: Search by name
    Given I am on the "Home Page"
    When I clear the form
    And I enter "Hat" in the "Name" field
    And I click the "Search" button
    Then I should see "Hat" in the results
    And I should not see "Shoes" in the results
    And I should not see "Big Mac" in the results
    And I should not see "Sheets" in the results

  Scenario: Search by category
    Given I am on the "Home Page"
    When I clear the form
    And I select "Food" from the "Category" list
    And I click the "Search" button
    Then I should see "Big Mac" in the results
    And I should not see "Hat" in the results
    And I should not see "Shoes" in the results
    And I should not see "Sheets" in the results

  Scenario: Search by availability
    Given I am on the "Home Page"
    When I clear the form
    And I select "True" from the "Availability" list
    And I click the "Search" button
    Then I should see "Hat" in the results
    And I should see "Big Mac" in the results
    And I should see "Sheets" in the results
    And I should not see "Shoes" in the results
