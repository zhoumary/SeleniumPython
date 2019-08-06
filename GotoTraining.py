# coding=utf-8

from selenium import webdriver
import time
import os

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
    login = s1Driver.find_element_by_id('logon_button')
    login.click()

    time.sleep(60)
    s1Url = s1Driver.current_url

    if s1Url:
        return s1Driver

def gotoTraining():
    s1 = login()
    if s1:
        # from team to training
        team = s1.find_element_by_id('__item0-__xmlview0--menu-0')
        team.click()
        time.sleep(6)

        training = s1.find_element_by_id('__item12-__xmlview5--sections-list-6-content')
        training.click()
        time.sleep(6)
        s1.quit()

def main():
    gotoTraining()

main()
