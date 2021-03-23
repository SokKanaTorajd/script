from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

class WebDriver:
    
    location_data = {}
    
    def __init(self):
        
        self.PATH = "chromedriver.exe"
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(self.PATH, options=self.options)
        
        self.location_data["rating"] = "NA"
        self.location_data["reviews_count"] = "NA"
        
    def get_location_data(self):
        
        try: 
            avg_rating = self.driver.find_element_by_class_name("section-star-display")
            total_reviews = self.driver.find_element_by_class_name("section-rating-term-list")
        except:
            pass
        
        try:
            self.location_data["rating"] = avg_rating.text
            self.location_Data["reviews_count"] = total_reviews.text[1:-1]
        except:
            pass
        
    # ngeklik all review button
    
    # def click_all_reviews_button(self):
    #     try:
    #         WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "allxGeDnJMl__button")))
            
    #         element = self.driver.find_element_by_class_name("allxGeDnJMl__button")
    #         element.click()
            
    #     except:
    #         self.driver.quit()
    #         return False
        
    #     return True
    
    # self scroll page review
    
    def scroll_the_page(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "section-layout-root"))) #waits for the page to load
            pause_time = 2 #waiting time after each scroll
            max_count = 5 #number of times we will scroll the scroll bar to the bottom
            x = 0
            
            while(x<max_count):
                scrollable_div = self.driver.find_element_by_css_selector('div.section-layout.section-scrollbox.scrollable-y.scrollable-show') #it gets the section of the scroll bar
                try: 
                    self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div) #scroll to the bottom
                except:
                    pass
                
                time.sleep(pause_time) #wait more reviews to load
                x=x+1
                
        except:
            self.driver.quit()
                
    #expand long reviews
    def expand_all_reviews(self):
        try:
            element = self.driver.find_elements_by_class_name("section-expand-review blue-link")
            for i in element:
                i.click()
        except:
            pass
        
    #scrape the data
    def get_reviews_data(self):
        
        try:
            review_text = self.driver.find_elements_by_class_name("section-review-review-content") #list of all html sections with the reviewer reviews
            review_stars = self.driver.find_elements_by_css_selector("[class='section-review-stars']") #list of all the html sections with the reviewer rating
            
            review_stars_final = []
            
            for i in review_stars:
                review_stars_final.append(i.get_attribute("aria-label"))
                
            review_text_list = [a.text for a in review_text]
            review_stars_list = [a for a in review_stars_final]
            
            for (a,b) in zip(review_text_list, review_stars_list):
                self.location_data["Reviews"].append({"review":a, "rating":b})
                
        except Exception as c:
            pass
        
    # final step
    
    def scrape(self, url): #passed the url as a variable
        try:
            self.driver.get(url)
        except Exception as c:
            self.driver.quit()
            return
        time.sleep(10) #waiting for the page to load.
        
        self.get_location_data()
        # if(self.click_all_reviews_button()==False):
        #    return(self.location_data)
       
        time.sleep(5)
        
        self.scroll_the_page()
        self.expand_all_reviews()
        self.get_reviews_data()
        
        self.driver.quit()
        
        return(self.location_data)

url = "https://www.google.com/maps/place/SEDJUK+Bakmi+%26+Kopi/@-6.2273722,106.81184,15z/data=!4m5!3m4!1s0x0:0xd54260c926073fad!8m2!3d-6.2273722!4d106.81184"
x = WebDriver()
print(x.scrape(url))