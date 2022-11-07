from selenium.webdriver.common.by import By
from time import sleep

class ProductDetails:
    def __init__(self,browser=None) -> None:
        self.browser = browser

    def get_links(self,URL):

        self.browser.get(URL)
        sleep(4)
        k = 1000
        self.browser.execute_script("window.scrollTo(0, {});".format(k))

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
        
        # name
        try:
            name = self.browser.find_element(By.XPATH,'//*[@class="_2rQP1z"]/span').text
            print("name",name)
        except:
            name = None
            print("name",name)
        
        # rating
        try:
            rating = self.browser.find_element(By.CSS_SELECTOR,"div._3y5XOB._14izon").text
            print("rating",rating)
        except:
            rating = None
            print("rating",rating)
        
        # evaluate
        try:
            evaluate = self.browser.find_elements(By.CSS_SELECTOR,"div._3y5XOB")[-1].text
            print("evaluate",evaluate)
        except:
            evaluate = None
            print("evaluate",evaluate)

        # sold
        try:
            sold = self.browser.find_element(By.CSS_SELECTOR,"div.HmRxgn").text
            print("sold",sold)
        except:
            sold = None
            print("sold",sold)

        # return details
        try:
            return_ = self.browser.find_elements(By.CSS_SELECTOR,"div._2xXtLT")[0].text
            print("return_",return_)
        except:
            return_ = None
            print("return_",return_)

        # genuine
        try:
            genuine = self.browser.find_elements(By.CSS_SELECTOR,"div._2xXtLT")[1].text
            print("genuine",genuine)
        except:
            evaluate = None
            print("genuine",genuine)

        # shipping
        try:
            shipping = self.browser.find_elements(By.CSS_SELECTOR,"div._2xXtLT")[2].text
            print("Shipping",shipping)
        except:
            shipping = None
            print("Shipping",shipping)
        
        # available
        try:
            available = self.browser.find_elements(By.XPATH,'//*[contains(@class,"flex items-center _283ldj")]/div')[-1].text
            print("Available", available)
        except:
            evaluate = None
            print("Available", available)

        # category
        try:
            # get categories list
            categories = self.browser.find_elements(By.CSS_SELECTOR,'a.CyVtI7')
            category = categories[1].text
            sub_category = categories[2].text + ">" + categories[3].text
            print("Category:", category,sub_category)
        except:
            category,sub_category = None,None

        # liked 
        try:
            liked = self.browser.find_element(By.CSS_SELECTOR,'div._11Toj4').text
            print("Liked", liked)
        except:
            liked = None
            print("Liked",liked)

        # trademark
        try:
            trademark = self.browser.find_element(By.CSS_SELECTOR,'div._8N1GCt').text
            print("trademark", trademark)
        except:
            liked = None
            print("trademark",trademark)

        response = {
            "Name": name,
            "category": category + ">" + sub_category,
            "Rating": rating,
            "Evaluate": evaluate,
            "Sold": sold,
            "Return": return_,
            "Genuine": genuine,
            "Shipping": shipping,
            "Available": available,
            "Liked": liked,
            "Trademark": trademark
        }

        return response


