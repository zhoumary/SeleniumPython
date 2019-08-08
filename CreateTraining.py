# coding=utf-8

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


# fitable for page jumping
class wait_for_page_load(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self,*_):
        wait_for_page_load(self.page_has_loaded)


# monitor wheather the element is loaded, just fitable in debug mode
def elementloaded(page, element):
    isElemLoaded = False
    while (isElemLoaded == False):
        if(page.find_element_by_id(element)):
            isElemLoaded = True
            return isElemLoaded
        else:
            elementloaded(page, element)


def login():
    s1Driver = webdriver.Chrome()
    s1Driver.get('https://sgassportsdevque8x3ffel.cn1.hana.ondemand.com')

    # create a username/password configure file
    userName = ''
    password = ''
    userFile = raw_input('打开用户信息文件 -> ')
    if os.path.isfile(userFile):
        with open(userFile,'r') as user_info:
            lines = user_info.readlines()
            for line in lines:
                if line.find('User Name:') != -1:
                    line = line.replace('\n','')
                    userNameColon = line.find(':')
                    userName = line[(userNameColon + 2):]
                elif line.find('Password:') != -1:
                    passwordColon = line.find(':')
                    password = line[(passwordColon + 2):]

        user_info.close()

    # post userName and password to Login Page
    loginUser = s1Driver.find_element_by_id('xs_username-inner')
    loginUser.send_keys(userName)
    loginPassword = s1Driver.find_element_by_id('xs_password-inner')
    loginPassword.send_keys(password)
    with wait_for_page_load(s1Driver):
        s1Driver.find_element_by_id('logon_button').click()

        if s1Driver:
            return s1Driver


# use webdriverwait to do the explicity
def detectElement(driver, delay, element):
    wait = WebDriverWait(driver, delay)
    isLoaded = wait.until(EC.presence_of_element_located((By.ID, element)))
    return isLoaded


class TestTraining(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestTraining, self).__init__(methodName)
        self.s1 = login()

    def test_gotoTraining(self):
        if self.s1:
            # from team to training, in the first page
            team = detectElement(self.s1, 100, '__item0-__xmlview0--menu-0')
            if (team):
                team.click()

            training = detectElement(self.s1, 10, '__item12-__xmlview5--sections-list-6-content')
            if (training):
                training.click()


            # click add training button
            addTraining = detectElement(self.s1, 30, '__button23-__toolbar2-0-inner')
            if (addTraining):
                addTraining.click()
                time.sleep(10)

    def exit(self):
        self.s1.quit()


if __name__ == '__main__':
    unittest.main()
