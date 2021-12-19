
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import time
from selenium.webdriver.common.keys import Keys


chromedriver="D:\Drivers\chromedriver_win32\chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
driver.get('https://www.amazon.in/')
driver.implicitly_wait(10)


element = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
element.send_keys("Samsung")
time.sleep(5)
button =driver.find_element(By.XPATH, "//input[@type='submit']")
button.click()
time.sleep(25)

mobile_names = driver.find_elements(By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']")
mobile_prices = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")

my_names=[]
my_prices=[]

for mobile in mobile_names:
    # print(mobile.text)
    my_names.append(mobile.text)

for price in mobile_prices:
    # print(price.text)
    my_prices.append(price.text)


dict=  {
        "Mobiles_name":my_names,
        "Mobiles_price":my_prices,
}

# new page products are stored into txt file.
y = json.dumps(dict)
with open('Mobiles_details.txt','a')as file:
    file.write(y)


# removing first item in a list & storing into another txt file.
list=[my_names,my_prices]
list[1]
print(list)

z = json.dumps(list)
with open('New_Mobiles_details.txt','a')as file:
    file.write(z)


driver.close()
driver.quit()