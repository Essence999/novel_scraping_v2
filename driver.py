from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class Driver():
    def __init__(self, link):
        self.driver = webdriver.Edge()
        self.driver.get(link)
        self.driver.minimize_window()
        self.chapters_titles = self.get_all_chapters()
        self.driver.quit()

    def get_all_chapters(self):
        self.go_to_first_chapter()
        sleep(1)
        return self.find('//*[@id="chr-nav-top"]/div/select').text

    def go_to_first_chapter(self):
        self.click('//*[@id="novel"]/div[1]/div[1]/div[3]/a')
        self.click('//*[@id="chr-nav-top"]/div/button/span')

    def find(self, xpath):
        element = self.driver.find_element(By.XPATH, f'{xpath}')
        return element

    def click(self, xpath):
        element = self.find(xpath)
        element.click()
        return element
