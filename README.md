# Pokemon-Web-Automation-Selenium-
Pokémon Web Automation with Selenium Python
This project demonstrates web automation testing on the official Pokémon website using Python and Selenium.
It simulates a real user journey to validate the main flow of the Pokédex feature.

🚀 Objective

Automate the following user flow on:
👉 https://www.pokemon.com/us/

- Navigate to Pokédex
- Search for a Pokémon
- View Pokémon details
- Explore more Pokémon

✅ Test Scenario (Acceptance Criteria)

The automation script covers the following steps:

- Open the Pokémon website
- Click CTA “Pokédex”
- Search for “Pikachu”
- Select “Pikachu” from the search results
- Scroll down to display all details about Pikachu
- Click CTA “Explore More Pokémon”
- Scroll down to display additional Pokémon

📌 Expected Result
Successfully navigates to Pokédex
Pikachu appears in search results
Pikachu detail page is displayed
Successfully navigates to Explore Pokémon page
Pokémon list is displayed after scrolling

🧰 Tech Stac
Python 3.x
Selenium
undetected-chromedriver
Google Chrome

🔍 Key Automation Techniques
Handling cookie popups
Explicit waits (WebDriverWait)
Scrolling into view
Handling dynamic elements (JavaScript-rendered UI)
Bypassing click interception (overlay issues)
