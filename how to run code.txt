To run the code:

pip install selenium
pip install tqdm
pip install webdriver_manager

{Run code by: python3 crawler.py}

NOTE:
# Enter user profile
Under crawler.py 

at the end:
obj = Crawling()
print(obj.get_user_posts("<user profile>"))


# ----------------------
# Remember to set num = (to a specific value), else it will crawl ALL the posts

under get_posts
num = 1000
# ----------------------

# Change file name to save scraped data
under get_posts
with open('<file name>.txt', 'w') as f:
    for item in posts:
        f.write("%s\n" % item)


# re-crawl the specific key provided
Under fetch.py
fetch_details_key 

to call re-crawl:
obj.read_file()
Remember to define the old file name and new file name
def read_file(self,old,new):
    with open(old, "r") as f:
        new_f = open(new, "w")

