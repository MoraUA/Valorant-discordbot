#imports
import time
import io
import os
from bs4 import BeautifulSoup
from chromedrivers import Driver

#function which clear html file 
#(we do this, because in parsing process we include all html tags from site to this file)
def clear_html_file():
    with open("index.html",'r+') as file:
        file.truncate(0)




def get_stats(player:str):
    nickname = ""
    tag = ""
    is_nickname = True

    for l in player:                 #split nickname and tag
        if(l == '#'):
            is_nickname = False
            continue
        if is_nickname:
            nickname+=l
        else:
            tag+=l
    
    url=f"https://tracker.gg/valorant/profile/riot/{nickname}%23{tag}/overview"

    try:
        stats = {
            '***Damage/Round***' : None,
            '***Kill/Death***' : None,
            '***HeadShot%***' : None,
            '***Win%***' : None,
            '***Wins***': None,
            '***Kills***'  : None,
            '***Deaths***' : None,
            '***Assists***' : None,
        }

        driver = Driver.create_driver()
        driver.get(url=url)
        time.sleep(2)

        file = io.open("index.html", mode="w", encoding="utf-8")    #writing whole source page to our html file
        file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    try:
        with open("index.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')  #find all values which we need
        stats_value = soup.find('body').find('div', class_='trn-wrapper').find('div', class_='trn-container').find('div', class_='trn-content').find('main').find('div', class_=('content', 'no-card-margin')).find('div', class_=('trn-grid', 'container')).find_all('span', class_='value')
        
    except Exception as ex:
        print(ex)
    finally:
        clear_html_file()
    try:
        for i, (k, v) in enumerate(stats.items()):
            stats[k] = stats_value[i+3].get_text()
    except Exception as ex:
        return {1 :"error"}

    return stats


