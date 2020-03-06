
from time import sleep

from tqdm import tqdm
import sys
import traceback
import json
import ast
from instagrambot import InstagramBot
from exceptions import *
from fetch import *

class Crawling():
    def __init__(self, has_screen=False):
        super(Crawling, self).__init__()
        self.bot = InstagramBot('learningIR2020', 'cz4034Insta')
        self.bot.signIn()

    def instagram_int(string):
        return int(string.replace(",", ""))

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
        # print("AHHH")
        # for my_href in photo:
        #     print(my_href.get_attribute("src"))
        statistics = [ele.text for ele in bot.find_element_by_css(".g47SY")]
        #print("Stats: ")
        #print(statistics)
        post_num, follower_num, following_num = statistics
        return {
            #"name": name.text,
            #"desc": desc.text if desc else None,
            "photo_url": photo[0].get_attribute("src"),
            "post_num": post_num,
            "url": url,
            #"follower_num": follower_num,
            #"following_num": following_num,
        }       
    def get_user_posts(self, username, number=None, detail=False):
        user_profile = self.get_user_profile(username)
        if not number:
            number = int(user_profile["post_num"].replace(",", ""))
            url = user_profile["url"]

        return self._get_posts(number)
    
    def _get_posts(self, num):
        """
            To get posts, we have to click on the load more
            button and make the browser call post api.
        """
        TIMEOUT = 600
        bot = self.bot
        key_set = set()
        posts = []
        pre_post_num = 0
        wait_time = 1
        
        # ----------------------
        # Remember to set num = (to a specific value), else it will crawl ALL the posts
        # ----------------------
        pbar = tqdm(total=num)
        num = 1000
        def start_fetching(pre_post_num, wait_time):
            ele_posts = bot.find_element_by_css(".v1Nh3 a")
            i=-1
            for ele in ele_posts:
                key = ele.get_attribute("href")
                i=i+1
                if key not in key_set:
                    dict_post = { "key": key }
                    ele_img = bot.find_element_by_css(".KL4Bh img", ele)
                    #dict_post["caption"] = ele_img.get_attribute("alt")
                    # dict_post["img_urls"] = ele_img[i].get_attribute("src")
                    # for i in ele_img:
                    #     print(i.get_attribute("src"))
                    #     dict_post["src"] = i.get_attribute("src")
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
        with open('straits_times_1000_.txt', 'w') as f:
            for item in posts:
                f.write("%s\n" % item)
        return posts[:num]

    # Call this function to re-crawl the specific data
    def read_file(self):
        with open("straits_times_1000.txt", "r") as f:
            
            print("HEre")
            bot = self.bot
            count = 0
            i = 1
            posts = []
            for post in f:
                #post = f.readline()
                res = ast.literal_eval(post) 
                print("--------------------------------- post number " + str(i))
                if (res.get("comments") == None or res.get("img_urls") == []):
                    #print(res["key"] + " no comments" )
                    new_post = fetch_details_key(bot,res["key"])
                    posts.append(new_post)
                else:
                    posts.append(post)
                i = i+1
                # if i== 3: break;  to test if it worked
             #Write everything (COMPLETE) crawl back
            print("WRITING")
            print(posts)
            new_f = open("new__straits_times_VIDEO.txt", "w")
            new_f.writelines("%s\n" % line for line in posts)
            # for item in posts:
            #     print("item")
            #     print(item)
            #     new_f.write("%s\n" % item)
            print("WRITING end")
            new_f.close()
    
    # Function not used
    def _get_posts_full(self, num, url):
        @retry()
        def check_next_post(cur_key):
            ele_a_datetime = bot.find_element_by_css(".eo2As .c-Yi7")

            # It takes time to load the post for some users with slow network
            if ele_a_datetime is None:
                raise RetryException()
            
            next_key = ele_a_datetime.get_attribute("href")
            if cur_key == next_key:
                raise RetryException()

        bot = self.bot
        bot.browser.implicitly_wait(1)
        bot.scroll_down()
        ele_post = bot.find_element_by_css(".v1Nh3 a")
        #ele_post.click()
        dict_posts = {}

        pbar = tqdm(total=num)
        pbar.set_description("fetching")
        cur_key = None

        all_posts = self._get_posts(num)
        i = 1

        # Fetching all posts
        for _ in range(num):
            dict_post = {}

            # Fetching post detail
            try:
                if(i < num):
                    check_next_post(all_posts[i]['key'])
                    i = i + 1

                # Fetching datetime and url as key
                ele_a_datetime = bot.find_element_by_css(".eo2As .c-Yi7")
                cur_key = ele_a_datetime.get_attribute("href")
                #dict_post["key"] = cur_key
                #fetch_datetime(bot, dict_post)
                #fetch_imgs(bot, dict_post)
                #fetch_likes_plays(bot, dict_post)
                #fetch_likers(bot, dict_post)
                #fetch_caption(bot, dict_post)
                #fetch_comments(bot, dict_post)

            except RetryException:
                sys.stderr.write(
                    "\x1b[1;31m"
                    + "Failed to fetch the post: "
                    + cur_key or 'URL not fetched'
                    + "\x1b[0m"
                    + "\n"
                )
                break

            except Exception:
                sys.stderr.write(
                    "\x1b[1;31m"
                    + "Failed to fetch the post: "
                    + cur_key if isinstance(cur_key,str) else 'URL not fetched'
                    + "\x1b[0m"
                    + "\n"
                )
                traceback.print_exc()

            self.log(json.dumps(dict_post, ensure_ascii=False))
            dict_posts[url] = dict_post

            pbar.update(1)

        pbar.close()
        posts = list(dict_posts.values())
        if posts:
            posts.sort(key=lambda post: post["datetime"], reverse=True)
        return posts

obj = Crawling()

# Crawl (num) data
#print(obj.get_user_posts("straits_times")) #Enter The Username u want to crawl

# Re-Crawl those links in the file that are incomplete
# 
obj.read_file()


