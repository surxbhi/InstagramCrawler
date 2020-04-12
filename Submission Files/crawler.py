from time import sleep
from tqdm import tqdm
import sys
import traceback
import json
import ast
from instagrambot import InstagramBot
from fetch import *
#******************************************************************
# CZ4034 2019/2020 
# Instagram Crawler 
# 
# Author: Surabhi Malani
# 
# References: https://github.com/huaying/instagram-crawler
#******************************************************************


class Crawling():
    def __init__(self, has_screen=False):
        super(Crawling, self).__init__()
        # Please enter username and password here
        self.bot = InstagramBot('learningIR2020', 'cz4034Insta') 
        #self.bot = InstagramBot('<username>', '<password>') 
        self.bot.signIn() # Bot signs in to instagram account

    # def instagram_int(string):
    #     return int(string.replace(",", ""))

    # Function goes to userprofile page and extracts profile specific information
    def get_user_profile(self, username):
        browser = self.bot.browser
        url = "https://www.instagram.com/"+username+"/"
        print(url)
        browser.get(url)
        bot = self.bot
        name = bot.find_element_by_css(".rhpdm")
        print("Name:")
        print(name)
        desc = bot.find_element_by_css(".-vDIg span")
        photo = bot.find_element_by_css("._6q-tv")
        statistics = [ele.text for ele in bot.find_element_by_css(".g47SY")]
        post_num, follower_num, following_num = statistics
        return {
            "photo_url": photo[0].get_attribute("src"),
            "post_num": post_num,
            "url": url,
        }       
    
    # Function extracts number of posts of account and calls crawler _get_posts() function
    def get_user_posts(self, username, number=None, detail=False):
        user_profile = self.get_user_profile(username)
        if not number:
            number = int(user_profile["post_num"].replace(",", ""))
            url = user_profile["url"]

        return self._get_posts(number)
    
    def _get_posts(self, num):
        TIMEOUT = 600
        bot = self.bot
        key_set = set()
        posts = []
        pre_post_num = 0
        wait_time = 1
        
        # -------------------------------------------------------------------------------
        # Remember to set num = (to a specific value), else it will crawl ALL the posts
        # -------------------------------------------------------------------------------
        num = 1 # Limit of posts to crawl
        pbar = tqdm(total=num)
        
        def start_fetching(pre_post_num, wait_time):
            ele_posts = bot.find_element_by_css(".v1Nh3 a")
            i=-1
            for ele in ele_posts:
                key = ele.get_attribute("href")
                i=i+1
                if key not in key_set:
                    dict_post = { "key": key }
                    ele_img = bot.find_element_by_css(".KL4Bh img", ele)
                    fetch_details(bot, dict_post)
                    key_set.add(key)
                    posts.append(dict_post)
                    if len(posts) == num:
                        break
            if pre_post_num == len(posts):
                pbar.set_description("Wait for %s sec" % (wait_time))
                sleep(15)
                pbar.set_description("fetching")
                wait_time *= 2
                bot.scroll_up(300)
            else:
                wait_time = 1
            pre_post_num = len(posts)
            bot.scroll_down()
            return pre_post_num, wait_time

        pbar.set_description("fetching")
        while len(posts) < num and wait_time < TIMEOUT:
            post_num, wait_time = start_fetching(pre_post_num, wait_time)
            pbar.update(post_num - pre_post_num)
            pre_post_num = post_num
            loading = bot.find_element_by_css(".W1Bne")
            if not loading and wait_time > TIMEOUT / 2:
                break
        print(posts)
        pbar.close()
        print("Done. Fetched %s posts." % (min(len(posts), num)))
        with open('test.txt', 'w') as f: # Change File Name
            for item in posts:
                f.write("%s\n" % item)
        return posts[:num]

    # Call this function to re-crawl those posts that do not contain comments
    def read_file(self):
        with open("<file name>.txt", "r") as f:
            print("Here")
            bot = self.bot
            count = 0
            i = 1
            posts = []
            for post in f:
                #post = f.readline()
                res = ast.literal_eval(post) 
                print("--------------------------------- post number " + str(i))
                if (res.get("comments") == None):#  or res.get("img_urls") == []  #Change if necessary
                    #print(res["key"] + " no comments" )
                    new_post = fetch_details_key(bot,res["key"]) # Recrawl data for the specific key with no comments / img_urls
                    posts.append(new_post)
                else:
                    posts.append(post)
                i = i+1
            #Write everything (COMPLETE) crawl back
            print("WRITING")
            print(posts)
            new_f = open("<file name>.txt", "w")
            new_f.writelines("%s\n" % line for line in posts)
            print("WRITING end")
            new_f.close()
    
    # Call this function to re-crawl those posts that do not contain video_urls and image_urls
    def get_video_file(self):
        with open("<file name>.txt", "r") as f:
            print("Here")
            bot = self.bot
            count = 0
            i = 1
            posts = []
            for post in f:
                #post = f.readline()
                res = ast.literal_eval(post) 
                print("--------------------------------- post number " + str(i))
                if (res.get("video_urls") != None or res.get("img_urls") != None ):
                    fetch_image_videos(bot,res,res["key"]) # Recrawl data for the specific key with no video / img_urls
                    posts.append(res)
                else:
                    posts.append(post)
            #Write everything (COMPLETE) crawl back
            print("WRITING")
            print(posts)
            new_f = open("<file name>.txt", "w")
            new_f.writelines("%s\n" % line for line in posts)
            print("WRITING end")
            new_f.close()


#----------- Create an object for crawling
obj = Crawling()

#----------- Crawl (num) data
print(obj.get_user_posts("nytimes")) #Enter The Username u want to crawl

#----------- Re-Crawl those links in the file that are incomplete comments
#obj.read_file()

#-----------Re-Crawl those links in the file that are incomplete video_url / image_url
#obj.get_video_file()
