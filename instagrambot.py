from time import sleep
import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class InstagramBot():
    def __init__(self, email, password):
        #self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
        self.email = email
        self.password = password
        
        # see if it works : Browser will Not Open, can run it background
        service_args = ["--ignore-ssl-errors=true"]
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--no-sandbox")
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chrome_options, service_args=service_args)
        
        
    def signIn(self):
            self.browser.get('https://www.instagram.com/accounts/login/')
            time.sleep(20)
            print("Done")
            emailInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
            passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
            emailInput.send_keys(self.email)
            passwordInput.send_keys(self.password)
            passwordInput.send_keys(Keys.ENTER)
            time.sleep(20)
            #self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            #print("scrolled")
            #time.sleep(10)
    def randmized_sleep(self, average):
        _min, _max = average * 1 / 2, average * 3 / 2
        sleep(random.uniform(_min, _max))
    def scroll_up(self, offset=-1, wait=2):
        if offset == -1:
            self.browser.execute_script("window.scrollTo(0, 0)")
        else:
            self.browser.execute_script("window.scrollBy(0, -%s)" % offset)
        #randmized_sleep(wait)
        time.sleep(1)
    def scroll_down(self, wait=0.3):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        #randmized_sleep(self, wait)
        time.sleep(1)
    def open_new_tab(self, url):
        self.browser.execute_script("window.open('%s');" %url)
        self.browser.switch_to.window(self.browser.window_handles[1])
    def close_current_tab(self):
        self.browser.close()

        self.browser.switch_to.window(self.browser.window_handles[0])

    def find_element_by_css(self, css_selector, elem = None, waittime = 0):
        obj = self.browser
        try:
            if waittime:
                WebDriverWait(obj, waittime).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
                )
        except TimeoutException:
            return None

        try:
            return obj.find_elements(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException:
            print("DId i come here ?")
            return None

