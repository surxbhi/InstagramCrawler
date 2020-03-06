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
print(obj.get_user_posts("<user profile>")  )


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


# To download all images / videos  
Look under Files to Download folder  

under img_urls in the csv if a post has multiple images, need to save them as    
| 1 2 | 4 | 
|-----|---|
| 3   |   |  
with a space between img_url / video_url  

with a space in the middle  

then the code runs, looks through ths csv, makes the nested list into a flat list, makes a dictionary file of original file name to new file name when we download the image using chrome extension, and also creates a file of original file name links to copy-paste and download the image/video files

