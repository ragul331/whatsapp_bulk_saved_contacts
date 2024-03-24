from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/home/username/.config/google-chrome")

driver = webdriver.Chrome(options=options)

driver.get('https://web.whatsapp.com/')
input("Press ENTER...")

image_path ="C:/logo p.png"  #Paste the document path

with open('msg.txt', 'r') as file:
    msg = file.read()
with open('names.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        time.sleep(1)
        try:
            button = driver.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[1]/p')
            button.click()
            actions2 = ActionChains(driver)
            actions2.key_down(Keys.LEFT_CONTROL).key_down(Keys.SHIFT).send_keys(
                Keys.HOME).key_up(Keys.CONTROL).key_up(Keys.SHIFT).send_keys(Keys.BACK_SPACE)
            actions2.perform()
            actions3 = ActionChains(driver)
            actions3.send_keys(n)
            actions3.perform()
            input('Enter...')
            actions = ActionChains(driver)
            time.sleep(1)
            button1 = driver.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]')
            button1.click()
            name_bar = driver.find_element(
                By.XPATH, '/html/body/div[1]/div/div[2]/div[4]/div/header/div[2]/div/div/div/span')
            name = name_bar.text
            if name==num:
                input()
                attach_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span')
                attach_button.click()
                doc_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[1]/li/div/input')
                doc_button.send_keys(image_path)
                time.sleep(2)
                actions = ActionChains(driver)
                for line in msg.split('\n'):
                    actions.send_keys(line)
                    actions.key_down(Keys.SHIFT).send_keys(
                        Keys.ENTER).key_up(Keys.SHIFT)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                time.sleep(4)
                print(num)
        except Exception as e:
            print(e)
