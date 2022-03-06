from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

option = int(input("Press\n1.Message\n2.Image"))

driver = webdriver.Chrome('chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)


def send_image():
    x_arg1 = '//div[@class="_26lC3"][@data-tab="10"]'
    wait.until(EC.presence_of_element_located((By.XPATH, x_arg1))).click()

    i_box = driver.find_element_by_xpath(
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
    )


    #Enter Image Path
    i_box.send_keys("C:\\Users\\Shub\\OneDrive\\Pictures\\Screenshots\\trial.png")

    g = '//div[@class="_165_h _2HL9j"]'
    send_button = wait.until(EC.presence_of_element_located((By.XPATH, g)))
    send_button.send_keys(Keys.ENTER)


def send_msz():
    string = "Hi, if this message is sent consider that ye ban gaya "

    inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="10"]'
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))

    input_box.send_keys(string + Keys.ENTER)


a = ['"Hay"', '"Ccc"']#contact or groups name must be in format '"Name"'

for target in a:
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
    if (option == 1):
        send_msz()
    elif (option == 2):
        send_image()
