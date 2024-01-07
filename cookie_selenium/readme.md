# Cookie Collector Automation

## Overview
Automate Cookie Clicker game using Python and Selenium. Earn coins, make upgrades, and enjoy the sweet success!

## Prerequisites
- Python 3.x
- Install Selenium: `pip install selenium`
- Download compatible web driver (e.g., ChromeDriver) and add to PATH

## Usage
1. Clone the repository: `git clone https://github.com/yourusername/cookie-collector.git`
2. Navigate to project folder: `cd cookie-collector`
3. Run script: `python cookie_collector.py`

## Configuration
- Set your Cookie Clicker game link in `cookie_collector.py`
- Customize upgrade conditions and strategies in the script

## Example
```python
# Set your game link
game_url = "https://orteil.dashnet.org/cookieclicker/"

# Customize upgrade strategy
if current_cookies >= 1000:
    make_upgrade("Cursor")
elif current_cookies >= 5000:
    make_upgrade("Grandma")
# Add more conditions as needed
```

## Disclaimer
For educational purposes only. Use responsibly and comply with the game's terms of service.

Happy automating! 🍪🤖
