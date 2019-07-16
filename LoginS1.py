# coding=utf-8

from selenium import webdriver
import time
import os
import codecs
from itertools import groupby
import json

s1Driver = webdriver.Chrome()
s1Driver.get('https://sgassportsdevque8x3ffel.cn1.hana.ondemand.com')

# create a username/password configure file
userName = ''
password = ''
userFile = raw_input('打开用户信息文件 -> ')
if os.path.isfile (userFile):
    with open(userFile,'r') as user_info:
        lines = user_info.readlines()
        for line in lines:
            if line.find('User Name:') != -1:
                line = line.replace('\n','')
                userNameColon = line.find(':')
                userName = line[(userNameColon + 2) : ]
            elif line.find('Password:') != -1:
                passwordColon = line.find(':')
                password = line[(passwordColon + 2) : ]


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


# test more analysis under analysis
analyses = s1Driver.find_element_by_id('__item2-__xmlview0--shell-2')
analyses.click()

time.sleep(8)
analyses = s1Driver.find_element_by_id('__item2-__item2-__xmlview0--shell-2-4-header')
analyses.click()

time.sleep(8)
report = s1Driver.find_element_by_id('__button71')
report.click()