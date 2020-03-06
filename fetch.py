from time import sleep
import re

def fetch_videos(bot,dict_post):
    video_url = set()
    #Fetch Video
    while True:
        ele_vid = bot.find_element_by_css("._97aPb video")
        if isinstance(ele_vid, list):
            for ele_img in ele_vid:
                video_url.add(ele_img.get_attribute("src"))
            else:
                break
    if (ele_vid != []):
        dict_post["video_urls"] = list(video_url)
        print("video url " + str(list(video_url)))

def fetch_details_key(bot,key):
        dict_post = { "key": key }
        bot.open_new_tab(key)
        sleep(3)
        img_urls = set()
        #Fetch Images
        while True:
            ele_imgs = bot.find_element_by_css("._97aPb img")
            if isinstance(ele_imgs, list):
                for ele_img in ele_imgs:
                    img_urls.add(ele_img.get_attribute("src"))
                else:
                    break
        dict_post["img_urls"] = list(img_urls)

        #Fetch videos
        fetch_videos(bot,dict_post)
        #Location
        loca = bot.find_element_by_css(".JF9hh a")
        location = bot.find_element_by_css(".O4GlU",loca)
        if location == None:
            dict_post["location"] = ""
        for k in location:
            #print(k.text)
            dict_post["location"] = k.text

        #DateTime
        ele_datetime = bot.find_element_by_css(".eo2As .c-Yi7 ._1o9PC")
        for k in ele_datetime:
            datetime = k.get_attribute("datetime")
            dict_post["datetime"] = datetime
            #print(datetime)

        #Fetch likes and views
        fetch_likes_plays(bot,dict_post)
        sleep(10)
        #Fetch Caption + Comments
        fetch_caption(bot, dict_post)
        sleep(10)
        
        bot.close_current_tab()
        return dict_post

def fetch_details(bot, dict_post):

        bot.open_new_tab(dict_post["key"])
        sleep(3)
        img_urls = set()
        #Fetch Images
        while True:
            ele_imgs = bot.find_element_by_css("._97aPb img")
            if isinstance(ele_imgs, list):
                for ele_img in ele_imgs:
                    img_urls.add(ele_img.get_attribute("src"))
                else:
                    break
        dict_post["img_urls"] = list(img_urls)
        fetch_videos(bot,dict_post)
        #Location
        loca = bot.find_element_by_css(".JF9hh a")
        location = bot.find_element_by_css(".O4GlU",loca)
        if location == None:
            dict_post["location"] = ""
        for k in location:
            #print(k.text)
            dict_post["location"] = k.text

        #DateTime
        ele_datetime = bot.find_element_by_css(".eo2As .c-Yi7 ._1o9PC")
        for k in ele_datetime:
            datetime = k.get_attribute("datetime")
            dict_post["datetime"] = datetime
            print(datetime)

        #Fetch likes and views
        fetch_likes_plays(bot,dict_post)
        sleep(10)
        #Fetch Caption + Comments
        fetch_caption(bot, dict_post)
        sleep(10)
        
        bot.close_current_tab()

def fetch_caption(bot, dict_post):
    ele_comments = bot.find_element_by_css(".eo2As .gElp9")
    comments = []
    print("Hey what is this: ")
    
    print("__")
    if (ele_comments == []):
        return
    temp_element = bot.find_element_by_css("div.C4VMK > span", ele_comments[0])
    #temp_element2 = bot.find_element_by_css("span", temp_element)
    authors = bot.find_element_by_css("a.sqdOP", ele_comments[0])
    author_list = []
    for a in authors[1:]:
        print(a.text)
        author_list.append(a.text)
    print(author_list)
    comment_list = []
    for element in temp_element:
        if element.text not in ['Verified','']:
            comment = element.text
            print("comment")
            print(comment)
            print("__")
            comment_list.append(comment)
            #else
    print("im here")
    for i in range(len(comment_list)):
        comment_obj = {"author": author_list[i], "comment": comment_list[i]}
        #fetch mention and hashtags:
        fetch_mentions(comment_list[i], comment_obj)
        fetch_hashtags(comment_list[i], comment_obj)
        comments.append(comment_obj)

    if comments:
        dict_post["comments"] = comments
        print(comments)

def fetch_mentions(raw_test, dict_obj):
    mentions = get_parsed_mentions(raw_test)
    if mentions:
        dict_obj["mentions"] = mentions

def fetch_hashtags(raw_test, dict_obj):
    hashtags = get_parsed_hashtags(raw_test)
    if hashtags:
        dict_obj["hashtags"] = hashtags

def get_parsed_mentions(raw_text):
    regex = re.compile(r"@([\w\.]+)")
    regex.findall(raw_text)
    return regex.findall(raw_text)
def get_parsed_hashtags(raw_text):
    regex = re.compile(r"#(\w+)")
    regex.findall(raw_text)
    return regex.findall(raw_text)

def fetch_likes_plays(bot, dict_post):
    likes = None
    el_likes = bot.find_element_by_css(".Nm9Fw > * > span")
    el_see_likes = bot.find_element_by_css(".HbPOm > * > span")
    print(el_see_likes)
    for like in el_likes:
            likes = like.text
            print(likes)

    if (el_see_likes != []): #not None
        print("I am here")
        el_plays = bot.find_element_by_css(".vcOH2 > span")
        print(el_plays)
        for play in el_plays:
            print(play.text)
            dict_post["views"] = int(play.text.replace(",", "").replace(".", ""))
            sleep(10)
        el_see_likes[0].click()
        sleep(10)
        el_likes = bot.find_element_by_css(".vJRqr > span")
        for like in el_likes:
            likes = like.text
            sleep(10)
        bot.find_element_by_css(".QhbhU")[0].click()

    elif el_likes is not None:
        for like in el_likes:
            likes = like.text

    dict_post["likes"] = (
        int(likes.replace(",", "").replace(".", "")) if likes is not None else 0
    )
