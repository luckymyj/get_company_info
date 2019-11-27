
import os

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.alert import Alert 


def alert_present(driver):
    alert_flag = EC.alert_is_present()(driver)
    return alert_flag

def alert_accept(driver):
    Alert(driver).accept()

def get_driver(url):
    option = webdriver.ChromeOptions()
    option.add_argument('--user-data-dir=C:\\Users\\luckymyj\\AppData\\Local\\Google\\Chrome\\User Data\\Default')

    driver = webdriver.Chrome(chrome_options=option)
    driver.maximize_window()
    driver.get(url)
    return driver

def get_element_by_css(temp_driver, temp_element_css, temp_element_text):
    
    rtn_find_element = ''
    try:
        all_element = temp_driver.find_elements_by_css_selector(temp_element_css)
    except NoSuchElementException:
        raise('-------输入css错误,未找到元素------')
        # return rtn_find_element
    
    all_element_text = []

    for each_element in all_element:
        all_element_text.append(each_element.text)
    
    # print(all_element_text)
    try:
        rtn_find_element = all_element[all_element_text.index(temp_element_text)]
    except ValueError:
        raise('-------输入查找元素错误,未找到元素------')
    
    return rtn_find_element


def get_element_text(temp_driver, temp_elements_css):

    all_elements = temp_driver.find_elements_by_css_selector(temp_elements_css)
    rtn_text_list = []
    try:

        for each_element in all_elements:
            rtn_text_list.append(each_element.text)
    
    except NoSuchElementException:
        raise('=====元素定位错误=======')

    return rtn_text_list

def get_element_by_css_re(temp_driver, temp_css, temp_text):

    all_element = temp_driver.find_elements_by_css_selector(temp_css)
    all_element_text = []

    for each_element in all_element:
        all_element_text.append(each_element.text)
    
    print(all_element_text)
    find_pattern = re.compile(temp_text+'\(\d+\)')

    find_element_text = ''
    for i in range(len(all_element_text)):
        if(find_pattern.findall(all_element_text[i])!=[]):
            find_element_text = all_element_text[i]
            break
        
    print(find_element_text)
    rtn_element = all_element[all_element_text.index(find_element_text)]
    return rtn_element

def get_dict_from_keyvalue(keys, *values):
    value_list = []
    for value in values:
          value_list.append(value)
    temp_dict = dict(zip(keys, value_list))
    return temp_dict


def wait_For_Exist(element_type, element, wait_time, driver, element_desc):
    
    if element_type == 'ID':
        by_tpye = By.ID
    elif element_type == 'CSS':
        by_type = By.CSS_SELECTOR
    elif element_type == 'XPATH':
        by_type = By.XPATH
    elif element_type == 'NAME':
        by_type = By.NAME
    try:
        fine_element = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((by_type, element))
        )
    except TimeoutException:
        raise('查找' + element_desc + '超时' + str(wait_time) + 's')


     
