# Instabot
Instagram bot that likes posts from followers

##Setup Clone this repository:
```
git clone https://github.com/SKoley89/Instabot.git
```

run the following command to install the required libraries:
```
pip install selenium
pip install bs4
```

Open Instabot.py

Get your Instagram credentials and add them to:
```
username = 'your_username'
password = 'your_password'
```
Download Chrome driver from:
https://chromedriver.chromium.org/

add you Chrome you path to:
```
driver = webdriver.Chrome('')
```

Enter Instagram urls for page you wish to scrape:
```
driver.get('')
```

Then run:
```
python Instabot.py
```
