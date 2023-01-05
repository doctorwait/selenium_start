from selenium import webdriver

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/find_link_text'
browser.get(link)
button = browser.find_element(by='link text', value='224592')
button.click()
input1 = browser.find_element(by='tag name', value='input')
input1.send_keys("Ivan")
input2 = browser.find_element(by='name', value='last_name')
input2.send_keys("Petrov")
input3 = browser.find_element(by='class name', value='city')
input3.send_keys("Smolensk")
input4 = browser.find_element(by='id', value='country')
input4.send_keys("Russia")
button = browser.find_element(by='css selector', value="button.btn")
button.click()
browser.quit()
