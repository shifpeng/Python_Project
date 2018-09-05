#http://hotels.ctrip.com/hotel/2537570.html
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import keys模块
# from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery
from bs4 import BeautifulSoup

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from config import *


browser = webdriver.Chrome(service_args=SERIVER_ARGS)
browser.maximize_window()  # 窗口最大化
wait = WebDriverWait(browser, 30)

def search():
    print('开始搜索')
    try:
        browser.get('http://hotels.ctrip.com/hotel/2537570.html')
        # 设置等待时间，等待网页响应
        # 提交按钮
        # submit = wait.until(EC.element_to_be_clickable((By.XPATH,
        #                                                 '//*[@id="site-content"]/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/button')))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_RoomListTbl > tbody > tr:nth-child(5) > td')))
        print("页面加载成功，开始获取数据")
        getHotelInfo()

    except TimeoutException:
        return search()
def getHotelInfo():


    soap=BeautifulSoup('','')
    html = browser.page_source  # 整个网页
    doc = PyQuery(html)
    items = doc('#J_RoomListTbl > tbody > tr').items()
    for item in items:
        product = {

        }
def main():
    total = search()
    # print(total)


if __name__ == '__main__':
    main()
# display.stop()