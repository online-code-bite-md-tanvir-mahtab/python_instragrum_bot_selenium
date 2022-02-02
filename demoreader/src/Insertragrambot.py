from telnetlib import EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# constant
USER_EMAIL = 'tanvir15-13433@diu.edu.bd'
USER_PASSWORD = '01955005706#@'

INSTRAGRAM_URI = 'https://www.instagram.com/accounts/login/'



# class
class Instragram:
    def __init__(self,edge_path):
        self.driver = webdriver.Edge(executable_path=edge_path)


    # creating the login automation method
    def login(self):
        try:
            self.driver.get(url=INSTRAGRAM_URI)
            sleep(2)
            email = self.driver.find_element_by_xpath(xpath='//*[@id="loginForm"]/div/div[1]/div/label/input')
            email.send_keys(USER_EMAIL)
            password = self.driver.find_element_by_xpath(xpath='//*[@id="loginForm"]/div/div[2]/div/label/input')
            password.send_keys(USER_PASSWORD)
            password.send_keys(Keys.ENTER)
            sleep(4)
            not_now = self.driver.find_element_by_xpath(xpath='//*[@id="react-root"]/section/main/div/div/div/div/button')
            not_now.send_keys(Keys.ENTER)
            sleep(4)
            # turn_off = self.driver.find_element_by_xpath(xpath='/html/body/div[6]/div/div/div/div[2]/h2')
            # print(turn_off.text)
            # sleep(4)
            turn_off = ui.WebDriverWait(self.driver,3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]')))
            print(turn_off.text)
            turn_off.click()
            sleep(4)
        except NoSuchElementException:
            self.driver.quit()
        pass

    # creating the flower finder method
    def find_flower(self):
        try:
            sleep(4)
            search = self.driver.get(url='https://www.instagram.com/python.hub/')
            sleep(4)
            folowers = self.driver.find_element_by_xpath(xpath='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
            folowers.click()
            sleep(4)
        except NoSuchElementException:
            self.driver.quit()
            

    # creating the folow clicker method
    def follower(self):
        try:
            sleep(10)
            list_of_people = self.driver.find_elements_by_css_selector(" .RnEpo  .pbNvD ._1XyCr  .isgrP .jSC57  li")
            for item in list_of_people:
                folowing = item.find_element_by_tag_name(name="button")
                sleep(1)
                folowing.click()
                sleep(4)
            sleep(4)
        except NoSuchElementException:
            sleep(1)
            self.driver.quit()