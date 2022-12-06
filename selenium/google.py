from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import time

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
elem = driver.find_element(By.NAME, "q")
searchTitle = '라바웨이브'
elem.send_keys(searchTitle)
elem.send_keys(Keys.RETURN)
imgList = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")
count = 1
for img in imgList:
    img.click()
    time.sleep(3)
    imgUrl = driver.find_element(By.CSS_SELECTOR,".n3VNCb").get_attribute("src")
    print(imgUrl)
    opener = urllib.request.build_opener()
    # 헤더에 햔제 시용하는 웹사이트랑 같은 헤더 추가
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    splitUrl = imgUrl.split('/')[1]
    print(splitUrl[:3])
    if splitUrl[:3] == 'png':
        urllib.request.urlretrieve(imgUrl,str(count)+".png")
    elif splitUrl[:3] == 'gif' or splitUrl[:4] == 'jpeg':
        urllib.request.urlretrieve(imgUrl,str(count)+".jpg")
    else :
        urllib.request.urlretrieve(imgUrl,str(count)+".svg")

    count = count + 1
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN) 엔터키
# assert "No results found." not in driver.page_source
# driver.close()
