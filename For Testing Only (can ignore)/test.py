from time import sleep
import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from instagrambot import *

bot = InstagramBot('', '!')
bot.signIn()
bot.browser.get("https://www.instagram.com/p/BCHXCaIpGZV-2DBfHCgTdbwRTVg0-8Qk2TLBVU0/")
el_see_likes = bot.find_element_by_css(".vcOH2")
el_plays = bot.find_element_by_css(".vcOH2 > span")
ele_comments = bot.find_element_by_css(".eo2As .gElp9")

temp_element = bot.find_element_by_css("span",ele_comments[0])
for element in temp_element:
    print("a")
    print(element.text)

print(el_plays)
for play in el_plays:
    print(play.text)
    view= int(play.text.replace(",", "").replace(".", ""))
    print("AH")
    print(view)
print(el_see_likes)
if (el_see_likes != []):
    el_see_likes[0].click()
sleep(5)
el_likes = bot.find_element_by_css(".vJRqr > span")
for like in el_likes:
    likes = like.text
    print(likes)
bot.find_element_by_css(".QhbhU")[0].click()
bot.browser.get("https://www.instagram.com/charlenelfj/")
key_set = set()
print("username")
#username = bot.browser.find_element_by_css_selector("a.FPmhX")
#print(username.text)
 
time.sleep(20)
print("location") 
ele_posts = bot.find_element_by_css(".v1Nh3 a")
ele=ele_posts[0]
ele_img = bot.find_element_by_css(".KL4Bh img", ele)
href = ele.get_attribute("href")
for i in ele_img:
    print(i.get_attribute("src"))
    
    bot.browser.get("https://www.instagram.com/p/BTRHRS_hs1b3VMU0bw227qyXisJERzHPXKWs100/")
    time.sleep(15)
    loca = bot.find_element_by_css(".JF9hh a")
    print(loca)
    location = bot.find_element_by_css(".O4GlU",loca)
    print("hm?")
    for k in location:
        print(k.text)
    #Fetch initial comment

    comments_elem = bot.find_element_by_css("ul.XQXOT")
    first_post_elem = bot.find_element_by_css(".ZyFrc", comments_elem)
    caption = bot.find_element_by_css("span", first_post_elem)
    for k in caption:
        print(k.text)
        print("Space")

    
    # location = bot.find_element_by_css(".O4GlU",loca)
    # print(location.text)
    break
# location = bot.find_element_by_css(".O4GlU")
# l = bot.browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/header/div[2]/div[2]/div[2]/a")
# href = l.get_attribute('href')
# print(href)
# print("mm") 
#location = bot.browser.find_element_by_css_selector("div#[class ='JF9hh'] a")
#print(location)
# print("H")
# print(location.text)
# for ele in location:
#     print(ele.text) 
#print(location.text)
#ele_posts = bot.find_element_by_css(".v1Nh3 a")
#ele_posts[0].click()
#i=0
# time.sleep(3)
# imgsrc= bot.browser.find_elements_by_xpath("/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/img")
# for ele in imgsrc:
#     x=ele.get_attribute("src")
#     print(x) 

#for i in range(50):
# time.sleep(3)
# imgsrc= bot.browser.find_elements_by_xpath("/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/img")
# for ele in imgsrc:
#     x=ele.get_attribute("src")
#     print("Img URL" + " "+ x) 

#-----
# time.sleep(3)
# print("here")
# dict_post={}
# ele_posts = bot.find_element_by_css(".v1Nh3 a")
# for ele in ele_posts:
#     key = ele.get_attribute("href")
#     if key not in key_set:
#         dict_post = { "key": key }
#         ele_img = bot.find_element_by_css(".KL4Bh img", ele)
#         for i in ele_img:
#             dict_post["src"] = i.get_attribute("src")
# print (dict_post) 
#-------
    # capsrc = bot.browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span")
    # for ele in imgsrc:
    #     x=ele.text
    #     print("Img Caption"+ i + " "+x) 
# for ele in ele_posts:
#     print(i)
#     i = i+1
#     key = ele.get_attribute("href")
#     if key not in key_set:
#         dict_post = { "key": key }
#         #ele_a_datetime = bot.find_element_by_css(".eo2As .c-Yi7")
#         #print(ele_a_datetime)
#         #ele_imgg = bot.find_element_by_css(".KL4BH .FFVAD")
#         #print(ele_imgg.get_attribute("src"))

#         print("Looking at picture")
#         #photolink = bot.browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/img")
#         #print(photolink.get_attribute("src"))
#         time.sleep(3)
#         imgsrc= bot.browser.find_elements_by_xpath("/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/img")
#         for ele in imgsrc:
#             x=ele.get_attribute("src")
#             print(x)  
#         #ele_img = bot.find_element_by_css(".KL4Bh img", ele)
#         #print(ele_img[0].get_attribute("src"))
#         #dict_post["caption"] = ele_img.get_attribute("alt")
#         #dict_post["img_url"] = ele_img.get_attribute("src")