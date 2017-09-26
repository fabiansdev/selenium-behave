Feature: Homepage
    Scenario: Successful login
        Given Im opening website
        then Im click log in button
        then Im typing my username
        then Im typing my password
        then Im submit log in