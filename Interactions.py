from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time


class Interactions:
    """
    This has all the  interaction functions like scrolling through followers and liking their posts
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('')
        self.hrefs = []
        
    
    def get_num_flw(self):
        flw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main')))
        sflw = b(flw.get_attribute('innerHTML'), 'html.parser')
        followers = sflw.findAll('span', {'class':'g47SY'})
        f = followers[1].getText().replace(',', '')
        if 'k' in f:
            f = float(f[:-1]) * 10 **3
            return f
        elif 'm' in f:
            f = float(f[:-1]) * 10**6
            return f
        else:
            return float(f)
    
    # 12 pages/loading*20 
    def get_followers(self):
        time.sleep(2)
        flw_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span')))
        flw_btn.click()
        self.popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/ul/div')))
        for h in range(11):
            time.sleep(1)
            print('scrolling')
            print(h)
            print('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)), self.popup)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)), self.popup)
            if h == 2:
                break

              
        for i in range (1):
            time.sleep(2)
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', self.popup)
        self.popup = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]')))
        b_popup = b(self.popup.get_attribute('innerHTML'), 'html.parser')
        for p in b_popup.findAll('li'):
            try:
                hlink = p.findAll('a')[0]['href']
                #after you get all of the links it stops so that you don't get extra data
                if 'div' in hlink:
                    return self.hrefs
                else:
                    self.hrefs.append(hlink)
            except:
                pass
        return self.hrefs


    def is_public(self):
        #If this returns true then it is most likely a public account
        try:
            astate = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div.Nd_Rl._2z6nI > article > div._4Kbb_ > div > h2')))
            if astate.text == 'This Account is Private':
                return False
            else:
                return True
        except:
            return True


    def liked_post(self):
         #If this returns tue then is is most likely an account with 0 posts
        try:
            p_text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > header > section > ul > li:nth-child(1) > span')))
            if p_text == '0':
                return False
            else:
                return True
        except:
            return True
        post = self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(1) > div:nth-child(1)')
        html = post.get_attribute('innerHTML')
        h = b(html, 'html.parser')
        href = h.a['href']
        self.driver.get('https://www.instagram.com' + href)
        like_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div')))
        like_btn.click()
       
            
        
        


        






   




        
    