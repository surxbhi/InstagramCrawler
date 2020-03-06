import json
import ast
from fetch import *
def read_file(username):
    f = open("sur_straits_times.txt", "r")
    post = f.readline()
    print("HEre")
    post = f.readline()
    print("HEre")
    print(post)
    #bot = self.bot
    #res = json.loads(post) 
    res = ast.literal_eval(post) 
    if res.get("comments") == None:
        print(res["key"] + " no comments" )
        #new_post = fetch_details_key(bot,res["key"])
        #print(new_post)

read_file("straits_times")