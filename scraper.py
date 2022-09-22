import csv
from operator import contains
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("D:\Code\Code\Selenium\chromedriver\chromedriver.exe"))

f=open("./text.csv", "w")

driver.implicitly_wait(5)
loginUrl="https://www.linkedin.com/login"
driver.get(loginUrl)
driver.find_element(By.XPATH,'.//*[@id="username"]').send_keys("tudsharma@gmail.com")
driver.find_element(By.XPATH, './/*[@id="password"]').send_keys("Tushar@0380")
sleep(5)
driver.find_element(By.XPATH, "./html/body/div/main/div[2]/div[1]/form/div[3]/button").click()

j=1
while True:
    url="https://www.linkedin.com/search/results/people/?geoUrn=%5B%22101165590%22%5D&origin=FACETED_SEARCH&page="+str(j)+"&sid=7Ws"
    j=j+1
    driver.get(url)
    profiles=driver.find_elements(By.CLASS_NAME,'reusable-search__result-container')
    i=1
    count=0
    for profile in profiles:
        linkClass=profile.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li['+str(i)+']/div/div/div[1]/div/a')        
        link=linkClass.get_attribute("href")
        


        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(link)
        try:
            detail=driver.find_element(By.XPATH,'//span[@aria-hidden="true" and text()="Experience"]')
            inUK=driver.find_elements(By.XPATH,'//span[@class="t-14 t-normal t-black--light"]/span[@aria-hidden="true" and contains(text(),"United Kingdom")]/parent::span//preceding-sibling::span[@class="t-14 t-normal t-black--light"]/span')
            for jobs in inUK:
                timeText=jobs.text
                time=timeText.split(" · ")[1]
                year=0
                if len(time)>7:
                    yr=time[0]
                year=year+int(yr)

            if year>3:
                raise Exception
        except Exception as e:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            i=i+1
            continue   
        f.write(link)
        print(link)
        f.write("\n")
        count=count+1
        driver.close()

        driver.switch_to.window(driver.window_handles[0])   
        i=i+1