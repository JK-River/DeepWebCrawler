# -*- coding:utf-8 -*-
from selenium import webdriver

def getKnowledge(keyWord):
    #目前谷歌知识图谱的语言只支持英文，需要设置hl=en
    url = '%s%s' % ("http://www.google.com/search?hl=en&q=",keyWord )
    browser = webdriver.Chrome()
    browser.get(url)
    knowledge = browser.find_element_by_id('extabar')
    print(knowledge.text)
    browser.quit()

if __name__ == '__main__':
    keyWord = '老虎体重是多少'
    getKnowledge(keyWord)
