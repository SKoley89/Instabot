from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import Interactions


#user credentials
username = 'your_username'
password = 'your_password'

#executing chrome web driver
driver = 0
# reference values
refs = []
max_likes = 350
max_follows = 50
def main():
    """
    Global variable for Chrome web driver
    """
    global driver
    print('running script..')
    driver = webdriver.Chrome('/Users/shouvick-koley/Desktop/InstaBot/chromedriver')
    l = login.Login(driver, username, password)
    l.signin()
    driver.get('')
    it = Interactions.Interactions(driver)
    refs = it.get_followers()
    print(it.get_num_flw())
    run_bot(refs, driver, it)

def run_bot(refs, driver, it):
    t = time.time()
    # how many pages were liked 
    L = 0
    # r is the href
    for r in refs:
        driver.get('https://www.instagram.com' + r)
        time.sleep(2)
        if it.get_num_flw() < 3000:
            if it.is_public():
                print('public account')
                print('current likes:' + str(L))
                if L < max_likes:
                    it.liked_post()
                    L += 1
                    print("Liked Post")
                else:
                    time.sleep(3600) # time.sleep(3600 - (time.time() - t)) -> t=t
            


   
    

if __name__ == '__main__':
    main()