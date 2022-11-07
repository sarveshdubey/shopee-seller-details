from selenium.webdriver.common.by import By
from time import sleep


class Details:
    def __init__(self,browser=None) -> None:
        self.browser = browser

    def seller_details(self,URL):

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
        

        try:
            self.browser.execute_script("arguments[0].click();", self.browser.find_element(By.CSS_SELECTOR,"div.shopee-avatar._1a-fH5"))
            sleep(1)
        except Exception as e:
            print("Number of pages not found:",e)

        try:
            # name
            try:
                name = self.browser.find_element(By.CSS_SELECTOR,"h1.section-seller-overview-horizontal__portrait-name").text
            except Exception as e:
                print("Name NaN:",e)
                name = "NaN"

            # active
            try:
                active = self.browser.find_element(By.CSS_SELECTOR,"div.section-seller-overview-horizontal__active-time").text
            except Exception as e:
                print("Active NaN:",e)
                active = "NaN"
            
            # 6 things
            try:
                ele = self.browser.find_elements(By.CSS_SELECTOR,"div.section-seller-overview__item-text-value")
                try:
                    products = ele[0].text
                except:
                    products = "NaN"

                try:
                    following = ele[2].text
                except:
                    following = "NaN"

                try:
                    chat_performance = ele[4].text
                except:
                    chat_performance = "NaN"

                try:
                    followers = ele[6].text
                except:
                    followers = "NaN"

                try:
                    rating = ele[8].text
                except:
                    rating = "NaN"

                try:
                    joined = ele[10].text
                except:
                    joined = "NaN"
            except Exception as e:
                print("Followers and other are none:",e)
                products = "NaN"
                following = "NaN"
                chat_performance = "NaN"
                followers = "NaN"
                rating = "NaN"
                joined = "NaN"

            # url and username
            try:
                sleep(1)
                url = self.browser.current_url
                username = url.split("/")[-1]
            except Exception as e:
                print("URL and Username is none",e)
                url = "NaN"
                username = "NaN"        
        except Exception as e:
            print("Failed to fetch details",e)

        print("Info:",name, followers, chat_performance, joined, rating, url, username, products, following)

        for k in range(1, 15000, 1000):
            sleep(0.5)
            self.browser.execute_script("window.scrollTo(0, {});".format(k))

        total_sold,total_products = 0, 0
        try:
            total_pages = self.browser.find_element(By.CLASS_NAME, "shopee-mini-page-controller__total")
            total_pages = int(total_pages.text)
            print("Total Pages:",total_pages)

            for i in range(0,total_pages):
                try:
                    product_section = self.browser.find_element(By.CLASS_NAME,"shop-page__all-products-section")
                except Exception as e:
                    print("No product section found",e)

                try:
                    product_cards = product_section.find_elements(By.CSS_SELECTOR,"div._3DGyGY")
                    products = len(product_cards)
                    total_products += products
                    # print("Products on this page/total products:",products,"/",total_products)
                except Exception as e:
                    print("Product cards not found",e)

                for card in product_cards:
                    try:
                        sold_ele = card.find_element(By.CSS_SELECTOR,"div._2Tc7Qg._2R-Crv").text
                        print("Sold Ele:",sold_ele)

                        sold_split = sold_ele.split(" ")
                        # print("sold_split :",sold_split)

                        for s in sold_split: 
                            res = True if next((chr for chr in s if chr.isdigit()), None ) else False
                            if res:
                                index = sold_split.index(s)
                                sold = sold_split[index]
                                break

                        try:
                            if "," in sold:
                                sold = sold.replace(",",".")
                                # print("If comma", sold)
                        except:
                            pass

                        if "k" in sold.lower():
                            sold = sold.replace("k","")
                            sold = int(float(sold) * 1000)
                            # print("If K:", sold)
                        else:
                            # print("Int value", sold)
                            sold = int(sold)
                        
                    except Exception as e:
                        sold = 0
                        print("Sold value: 0")

                    total_sold += sold

                try:
                    self.browser.execute_script("arguments[0].click();",
                        self.browser.find_element(By.CSS_SELECTOR,"button.shopee-button-outline.shopee-mini-page-controller__next-btn"))
                    sleep(4)
                except Exception as e:
                    print("Failed to click next button",e)
        except Exception as e:
            total_products,total_sold = "Nan", "Nan"
            print("Failed to get details",e)

        try:
            # clicking first product
            self.browser.execute_script("arguments[0].click();",
                self.browser.find_elements(By.CSS_SELECTOR,'div._3ZU4Xu')[0])
            sleep(10)
        except Exception as e:
            print("Product not clicked:",e)

        try:
            # get categories list
            categories = self.browser.find_elements(By.CSS_SELECTOR,'a.CyVtI7')
            category = categories[1].text
            sub_category = categories[2].text
        except Exception as e:
            category,sub_category = None,None
            print("Category and Sub-category not found",e)

        response = {
                        "Name": name,
                        "Followers": followers,
                        "Chat": chat_performance,
                        "Joined": joined,
                        "Rating": rating,
                        "URL": url,
                        "Username": username,
                        "Products": products,
                        "Following": following,
                        "Active": active,
                        "Total Products": total_products,
                        "Total Sold": total_sold,
                        "Category": category,
                        "Sub-category": sub_category,
                    }
        return response


        