from selenium.webdriver.common.by import By
from time import sleep

class Links:
    def __init__(self,browser=None) -> None:
        self.browser = browser

    def get_links(self,URL):

        self.browser.get(URL)
        sleep(4)

        # english
        try:
            english = self.browser.find_element(By.XPATH,
            '//button[contains(text(),"English")]')
            self.browser.execute_script("arguments[0].click();",english)
            sleep(2)
        except:
            pass

        # 404 
        try:
            over_18 = self.browser.find_element(By.XPATH,'//*[contains(text(),"It looks like something")]')
            print("Found 404")
            response = "404"
            return response
        except:
            pass
        
        # something in Vietnamise
        try:
            over_18 = self.browser.find_element(By.XPATH,'//*[contains(text(),"Sản phẩm này không tồn tại")]')
            print("Found 404 in Vietnamese")
            response = "404VN"
        except:
            pass
        
        # if login comes
        try:
            over_18 = self.browser.find_element(By.XPATH,'//*[@type="password"]')
            print("Login found:")
            response = "login"
            return response       
        except:
            pass
        
        # cancel the pop up
        try:
            pop_up = self.browser.find_element(By.CLASS_NAME,"home-popup__close-button")
            print("Pop was there")
            self.browser.execute_script("arguments[0].click();",pop_up)
            sleep(3)
        except:
            pass
        
        # over 18
        try:
            over_18 = self.browser.find_element(By.CSS_SELECTOR,
            "button.btn.btn-solid-primary.btn--m.btn--inline.shopee-alert-popup__btn")
            print("Over 18")
            self.browser.execute_script("arguments[0].click();",over_18)
            sleep(3)
        except:
            pass

        for k in range(1, 20000, 2000):
            sleep(0.5)
            self.browser.execute_script("window.scrollTo(0, {});".format(k))

        links_list = []
        links = self.browser.find_elements(By.XPATH, '//*[@data-sqe="link"]')

        for l in links:
            links_list.append(l.get_attribute("href"))

        response = links_list

        return response
