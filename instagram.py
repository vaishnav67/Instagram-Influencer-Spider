import re
import sys
import json
import time
import random
from graph import Graph
from selenium import webdriver
from py2neo import Graph as NeoGraph
def getFollowing(username):
    driver.get('https://www.instagram.com/'+username+'/?hl=en')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    page_followers = driver.find_element_by_xpath("//a[@href = '/"+username+"/following/']")
    page_followers.click()
    time.sleep(2)
    fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
    scroll = 0
    cur=0
    prev=0	
    while True or scroll!=30:
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        if(scroll%5==0):
            time.sleep(1)
            cur=driver.execute_script('return arguments[0].scrollTop;', fBody)
            if(cur==prev):
                break
            prev=cur
        scroll += 1
    # usernames = driver.find_elements_by_css_selector('a.FPmhX.notranslate._0imsa')
    # following = [users.text for users in usernames]
    # verified = driver.find_elements_by_css_selector('span.mTLOB.Szr5J.coreSpriteVerifiedBadge')
    # check = [users.text for users in verified]
    following=[]
    verified=[]
    usernames = driver.find_elements_by_css_selector('li.wo9IH')
    for i in usernames:
        try:
            username = i.find_element_by_css_selector('a.FPmhX.notranslate._0imsa')
            following.append(username.text)
            verify = i.find_element_by_css_selector('span.mTLOB.Szr5J.coreSpriteVerifiedBadge')
            verified.append(verify.text)
        except:
            verified.append("Not Verified")
    return(following, verified)
if __name__=="__main__":
    username=sys.argv[1]
    password=sys.argv[2]
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(4)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath('//button[normalize-space()="Log In"]').click()
    time.sleep(5)
    driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
    following,verified=getFollowing(username)
    graph=Graph()
    graph.del_graph()
    graph.add_node(username, 'Not Verified')
    for i in range(0,len(following)):
        graph.add_node(following[i],verified[i])
        graph.add_edge(username,following[i],'Not Verified',verified[i])
    for i in range(0,len(following)):
        if(verified[i]=='Not Verified'):
            try:
                fol,ver=getFollowing(following[i])
                for j in range(0,len(fol)):
                    if(fol[j] not in following):
                        graph.add_node(fol[j],ver[j])
                    graph.add_edge(following[i],fol[j],verified[i],ver[j])
            except:
                print("Couldn't retrieve data from "+following[i])
