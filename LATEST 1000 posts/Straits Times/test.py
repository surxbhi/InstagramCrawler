import ast
import pandas as pf

# with open("straits_times_1000.txt", "r") as f:
#     i = 0
#     for post in f:
#         res = ast.literal_eval(post) 
#         i = i+ 1
#         break;

x = "['https://instagram.fsin7-1.fna.fbcdn.net/v/t51.2885-15/fr/e15/s1080x1080/88276765_204693694274146_1237188978082252529_n.jpg?_nc_ht=instagram.fsin7-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=2Q2mA3ecfUoAX9PMDnt&oh=5c57dcb1933c0e682d99f45a812d8613&oe=5E8DDEE1']"

x = ast.literal_eval(x)

print(x)
print(type(x))