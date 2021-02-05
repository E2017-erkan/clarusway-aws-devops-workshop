from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\toshıba\\Desktop\\chromedriver_win32\\chromedriver")
base_url = "https://clarusway.com"
expected_title = "Home - Clarusway"
actual_title = ""
driver.get(base_url)
actual_title = driver.title
if actual_title == expected_title :
    print("Test Passed")
else:
    print("Test Failed")
driver.close()