from selenium import webdriver

wwW=webdriver.Chrome("chromedriver.exe")
urL="https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
wwW.implicitly_wait(10)
wwW.get(urL)
wwW.maximize_window()
buttoN=wwW.find_element_by_class_name("btn-big")
buttoN.click()

for mySoup in wwW.find_elements_by_class_name("r-ent"):
    try:
        print("日期: ",mySoup.find_element_by_class_name("date").text.strip())
        print(mySoup.find_element_by_class_name("title").text.strip())
        print("https://ptt.cc"+mySoup.find_element_by_tag_name("a").get_attribute("href"))
        print("作者: ",mySoup.find_element_by_class_name("author").text.strip())
        print("推文: ",mySoup.find_element_by_class_name("nrec").text.strip())
        print("==================================================")
    except:
        continue
wwW.quit()
