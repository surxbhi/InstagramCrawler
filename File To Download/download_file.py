
import pandas as pd
import ast

def parse_video_link_names(link_urls):
    link_row = {}
    all_link_names = []

    for linkurl in link_urls:
        original_name = linkurl
        link_name = linkurl.split("/")[5].split("?")[0]
        link_row = {"key": link_name} #the file name
        link_row["original_link_name"] = original_name #the file name to change it too
        all_link_names.append(link_row)
    return all_link_names

#video_link_urls = ["https://instagram.fsin5-1.fna.fbcdn.net/v/t50.16885-16/10000000_490583578320555_5737931685223037703_n.mp4?_nc_ht=instagram.fsin5-1.fna.fbcdn.net&_nc_cat=103&_nc_ohc=OEw_1Cbznt4AX_e88C1&oe=5E634D57&oh=0f6126922445566f901f113f8e891b25","https://instagram.fsin5-1.fna.fbcdn.net/v/t50.16885-16/10000000_564845857408669_5441359410436796881_n.mp4?_nc_ht=instagram.fsin5-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=C40SooeQ9DcAX9W8COs&oe=5E6327F2&oh=ac83905b84ceb351796ffc04cefc73f1"]

#print(parse_video_link_names(video_link_urls))

image_link_urls = ['https://instagram.fsin7-1.fna.fbcdn.net/v/t51.2885-15/e35/72528814_2858512947534984_6276343699501563998_n.jpg?_nc_ht=instagram.fsin7-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=0WRcMdq8bDEAX8uo32z&oh=709d0ec73e3f64fafef609ad2f278fcc&oe=5E963ECA','https://instagram.fsin7-1.fna.fbcdn.net/v/t51.2885-15/e35/72218524_733909833754382_7603134108743860204_n.jpg?_nc_ht=instagram.fsin7-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=3QZVm708wqwAX-H3Ay0&oh=43251a0cb94af21fbccffeb8039a5517&oe=5E93D131']
def parse_image_link_names(link_urls):
    link_row = {}
    all_link_names = []
    for linkurl in link_urls:
        original_name = linkurl
        link_name = linkurl.split("/")[6].split("?")[0]
        link_row = {"key": link_name} #the file name
        link_row["original_link_name"] = original_name #the file name to change it too
        print(link_row["original_link_name"])
        all_link_names.append(link_row)
    return all_link_names
#x = (parse_image_link_names(image_link_urls))
#print(x[0])
def flatten_list(l):
    flat_list = []
    for sublist in l:
        print("sublist")
        print(sublist)
        print (type(sublist))
        list_them = sublist.split(" ")
        for item in list_them:
            if (item != " "):
                flat_list.append(item)
    print(flat_list)
    return flat_list
def the_main_freaking_function(csv_file):
    #all_image_names = parse_image_link_names
    #all_video_names = parse_video_link_names
    #for filename in os.listdir("straits_times_images"):
    files = csv_file +".csv"
    df = pd.read_csv(files)
    # save_img_url = df["img_urls"].tolist()
    # print(save_img_url)
    # print(len(save_img_url))
    # print("hmm")
    # print("FLATTEN image LIST")
    # flat_image_list = flatten_list(save_img_url)
    # print(len(flat_image_list))
    # all_image_names = parse_image_link_names(flat_image_list)
    # print("All image names")
    # print(all_image_names)

    #Videos
    save_vid_url = df["video_urls"].tolist()
    print(save_vid_url)
    print(len(save_vid_url))
    print("hmm")
    print("FLATTEN video LIST")
    flat_vid_list = flatten_list(save_vid_url)
    print(len(flat_vid_list))
    all_vid_names = parse_video_link_names(flat_vid_list)
    print("All Video names")
    print(all_vid_names)

    #Write to file
    print("WRITING")
    new_f = open("straits_times_img_video_name.txt", "w")
    #new_f.writelines("%s\n" % line for line in all_image_names)
    new_f.writelines("%s\n" % line for line in all_vid_names)
    print("WRITING end")
    new_f.close()
    posts = []
    with open("straits_times_img_video_name.txt", "r") as f:
        print("HEre")
        i = 1
        for post in f:
            #post = f.readline()
            res = ast.literal_eval(post) 
            print("--------------------------------- post number " + str(i))
            i= i+1
            name = res.get("original_link_name")
            posts.append(name)
            print(name)
    print("WRITING")
    new_f_ = open("files_to_download.txt", "w")
    new_f_.writelines("%s,\n" % line for line in posts)
    print("WRITING end")
    new_f_.close()
the_main_freaking_function("csv_file")   