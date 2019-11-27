from util import wait_For_Exist
from util import get_driver
from util import get_element_by_css
from util import get_element_text
from util import alert_present
from util import alert_accept

import os
import time
import random

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
savedata_filepath = os.path.join(BASE_PATH, 'company_info.yaml')

gsxt_url = 'http://www.gsxt.gov.cn/index.html'
more_link_css = '.hot_a>a'
main_page_css = '.header_box a.menu_item .icon_01'
hotbyday_company_li_css = 'div#day_div li>a>div'
hotbyweek_company_li_css = 'div#week_div li>a>div'
hotbymonth_company_li_css = 'div#month_div li>a>div'

company_name_css = '.companyName>.fullName'
company_regNum_css = '.regNum_inner>i'
primaryInfo_item_css = '#primaryInfo>div[class="details clearfix"] dl>dt'
primaryInfo_result_css = '#primaryInfo>div[class="details clearfix"] dl>dd'

driver = get_driver(gsxt_url)
wait_For_Exist('CSS', more_link_css, 5, driver, '等待更多链接')

driver.find_element_by_css_selector(more_link_css).click()
driver.implicitly_wait(5)
gsxt_wins = driver.window_handles
driver.switch_to.window(gsxt_wins[1])
wait_For_Exist('CSS', hotbyday_company_li_css, 5, driver, '等待跳转页')
company_list = get_element_text(driver, hotbyday_company_li_css)

primaryInfo = []
for i in range(5):
    company_element = get_element_by_css(driver, hotbyday_company_li_css, company_list[i])
    time.sleep(random.randint(0,5))
    company_element.click()
    wait_For_Exist('CSS', company_name_css, 5, driver, '等待显示公司名称')
    alert_flag = alert_present(driver)
    # print(alert_flag)
    if alert_flag == True:
        driver.switch_to.alert_accept
        alert_accept(driver)
    each_company_items = get_element_text(driver, primaryInfo_item_css)
    each_company_results = get_element_text(driver, primaryInfo_result_css)
    # print(each_company_items)
    # print(each_company_results)
    primaryInfo.append(dict(zip(each_company_items, each_company_results)))
    
    driver.back()
    wait_For_Exist('CSS', hotbyday_company_li_css, 5, driver, '等待返回热搜页面')

for each_win in gsxt_wins:
    driver.switch_to.window(each_win)
    driver.close()

print(primaryInfo)
yamlwr = YamlSave(savedata_filepath)
yamlwr.save_data(primaryInfo)