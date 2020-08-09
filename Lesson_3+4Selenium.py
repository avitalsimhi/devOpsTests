from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path= "C:\\Users\\simchi\\Desktop\\chromedriver.exe")
driver.get("https://translate.google.co.il/")
driver.implicitly_wait(10)
print(driver.current_url)
print(driver.title)
element = driver.find_element_by_id("source")
# element.click()
if element.is_enabled():
    element.send_keys("שלום")
    element.send_keys(Keys.ENTER)

driver.execute_script("argumaent[0].click();", driver.find_element_by_id("source"))
elements = driver.find_elements_by_id("source")
print(len(elements))
elements = driver.find_elements_by_tag_name("div")
print(len(elements))
#כללי אצבע למציאת locators
#לוקיטור יוניקי
#לוקיטור שהכי פחות משתנה
# driver.find_element_by_partial_link_text()
#print(driver.page_source)
#driver.close()
driver.quit()
# driver.back()
# driver.forward()
# driver.refresh()
