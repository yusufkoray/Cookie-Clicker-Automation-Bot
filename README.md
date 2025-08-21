
# Cookie Clicker Automation Bot

This project is a simple automation bot for the Cookie Clicker game (https://ozh.github.io/cookieclicker/) using Python and Selenium. 

## Features
- Continuously clicks the big cookie to earn cookies.
- Every X seconds (default: 20s), checks the list of purchasable upgrades.
- Buys the most expensive upgrade that is affordable automatically.
- Handles product titles and prices dynamically to avoid errors with owned items.

## Requirements
- Python 3.x
- Selenium (`pip install selenium`)
- ChromeDriver installed and in PATH
- Google Chrome browser

## How to Run
1. Clone this repository:
   ```
   git clone <repo_url>
   ```
2. Install dependencies:
   ```
   pip install selenium
   ```
3. Run the bot:
   ```
   python cookie_clicker_bot.py
   ```

## Notes
- The bot opens a Chrome browser window that stays open after the script finishes (`detach=True` option).
- Make sure the game page is fully loaded before the bot starts clicking.
- You can adjust `check_time` to control how often the bot checks for upgrades.
