from smtpd import Options
from selenium import webdriver
#1
driver = webdriver.Chrome(executable_path= "C:\\Users\\simchi\\Desktop\\chromedriver.exe")
driver.get("http://www.walla.co.il")

driver = webdriver.Firefox(executable_path= "http://www.ynet.co.il")
driver.get("http://www.walla.co.il")

#2
driver = webdriver.Chrome(executable_path= "C:\\Users\\simchi\\Desktop\\chromedriver.exe")
driver.get("http://www.walla.co.il")
title = "וואלה"
driver.refresh()
if driver.title == title:
    print("Very Good!")

#3
# Yes

#4
driver = webdriver.Chrome(executable_path= "C:\\Users\\simchi\\Desktop\\chromedriver.exe")
driver.get("https://translate.google.co.il/")
element = driver.find_element_by_id("source")
if element.is_enabled():
    element.send_keys("שלום")

#5
driver = webdriver.Chrome(executable_path= "C:\\Users\\simchi\\Desktop\\chromedriver.exe")
driver.get("https://www.google.co.il/")
search = driver.find_element_by_name("q")
search.send_keys("חדשות")
btn = driver.find_element_by_name("btnK")
btn.click()

#6
driver = webdriver.Chrome(executable_path= "C:\\Users\\simchi\\Desktop\\chromedriver.exe")
driver.get("https://translate.google.co.il/")
element_1 = driver.find_element_by_id("source")
element_2 = driver.find_element_by_name("source")
element_3 = driver.find_element_by_xpath("//textarea[@autocapitalize='off']")
print(element_1)
print(element_2)
print(element_3)

#7
driver.get("https://www.facebook.com/")
driver.find_element_by_id("username").send_keys("ab@ab.com")
driver.find_element_by_id("password").send_keys("1q2w3e4r5t")


from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path= "C:\\Users\\simchi\\Desktop\\chromedriver.exe")
driver.delete_all_cookies()
print(driver.get_cookies())

driver = webdriver.Chrome(executable_path= "C:\\Users\\simchi\\Desktop\\chromedriver.exe")
driver.get("https://github.com/")
ele = driver.find_element_by_xpath("//input[@placeholder='Search GitHub']")
ele.send_keys(Keys.ENTER)

# מצאתי קוד באינטרנט בלי להבין מה המטרה בקוד הזה...
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

def main():
        opening = True
        while opening:
                try:
                        chrome_options = Options()
                        #Path to AdBlock
                        chrome_options.add_extension('/usr/local/bin/AdBlock_v.crx')
                        driver = webdriver.Chrome(chrome_options=chrome_options)
                except:
                        print('An unkown error has occured. Trying again...')
                else:
                        opening = False

        disable_adblocker(driver)


def click_element(driver, xpath, index):
        getting = True
        not_found_times = 0
        while getting:
                try:
                        getting = False
                        element = WebDriverWait(driver, 5).until(
                            EC.presence_of_all_elements_located((By.XPATH,xpath)))[index]
                        element.click()
            #driver.get(element.get_attribute("href"))


            #In case the page does not load properly
                except TimeoutException:
                        not_found_times += 1
                        if not_found_times < 2:
                                driver.refresh()
                                getting = True
                        else:
                                raise

            #In case DOM updates which makes elements stale
                except StaleElementReferenceException:
                        getting = True


def disable_adblocker(driver):
        driver.get('chrome://extensions')
        ad_blocker_xpath = '//div[@id="gighmmpiobklfepjocnamgkkbiglidom"]//div[@class="enable-controls"]//input'
        click_element(driver,ad_blocker_xpath,0)
        print('')


main()