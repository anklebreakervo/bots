from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://catalog.sjlibrary.org/iii/cas/login?service=https%3A%2F%2Fdiscover.sjlibrary.org%3A443%2Fiii%2Fencore%2Fj_acegi_cas_security_check")
driver.find_element_by_xpath('//*[@id="name"]').send_keys('Andrew Vo')
print("Entering name...")
driver.find_element_by_xpath('//*[@id="code"]').send_keys('21197700786402')
print("Entering library card number...")
driver.find_element_by_xpath('//*[@id="pin"]').send_keys('0852')
driver.find_element_by_xpath('//*[@id="fm1"]/div[5]/a/div/div/span/span').click()