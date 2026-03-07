from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.maximize_window()
# # 1. Open Amazon and print all category names
# driver.get("https://www.amazon.in")
# sleep(3)
# categories = driver.find_elements("xpath", "//div[@id='nav-xshop']//a")
# for cat in categories:
#     print(cat.text)
# sleep(20)

# #2.	 Print top 10 movie names from IMDB Top 250
# driver.get("https://www.imdb.com/chart/top/")
# sleep(3)
# movies = driver.find_elements("xpath", "//ul[contains(@class,'ipc-metadata-list')]//h3")
# for i in range(10):
#     print(movies[i].text)
# sleep(3)

# # 3.	Count all images on amazon
# driver.get("https://www.amazon.in/")
# sleep(4)
# a=driver.find_elements("tag name", "img")
# print(len(a))
# sleep(2)

# # 4.	Open https://demoqa.com/select-menu Target first dropdown in that page and select first option
# driver.get("https://demoqa.com/select-menu")
# sleep(2)
# a = Select(driver.find_element(By.ID,"withOptGroup"))
# a.select_by_index(1)
# sleep(2)

# # 5.	Print All Links in amazon Page
# driver.get("https://www.amazon.in")
# sleep(3)
# links = driver.find_elements(By.TAG_NAME,"a")
# for i in links:
#     print(i.get_attribute("href"))
# sleep(3)

# # 6.	Print Auto Suggestions of any site
# driver.get("https://www.google.com")
# driver.find_element(By.NAME,"q").send_keys("selenium")
# sleep(3)
# suggestions = driver.find_elements("xpath","//ul[@role='listbox']//li")
# for i in suggestions:
#     print(i.text)
# sleep(3)

# # 7.	From the “Accounts & Lists” section on the Amazon homepage, select the “Your Wish List” option.
#
# driver.get("https://www.amazon.in")
# sleep(3)
# account = driver.find_element(By.ID,"nav-link-accountList")
# action = ActionChains(driver)
# action.move_to_element(account).perform()
# sleep(2)
# driver.find_element(By.LINK_TEXT,"Your Wish List").click()
# sleep(4)

# # 8.	Access the content displayed inside the embedded page and print the heading text visible inside it.
# driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
# sleep(3)
# driver.switch_to.frame("iframeResult")
# driver.switch_to.frame(0)
# heading = driver.find_element(By.TAG_NAME,"h1").text
# print(heading)
# sleep(4)

# # 9.	Search Laptop and print all product titles.
driver.get("https://www.amazon.in")
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Laptop")
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(3)
titles = driver.find_elements(By.XPATH,"//h2/a/span")
for i in titles:
    print(i.text)

sleep(10)
driver.quit()