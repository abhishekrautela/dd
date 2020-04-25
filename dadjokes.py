import requests as rq
import random as rn

joke = input("Let me tell you  a joke! Give me a topic: ")
    
res = rq.get("http://icanhazdadjoke.com/search",headers={
        'Accept':'application/json'},params={
                "term":joke})
try:
    if(res.json()['total_jokes']>0):
        
        print(f"I found {res.json()['total_jokes']} jokes on {joke}, Here's one:")
        print(rn.choice(res.json()['results'])['joke'])
    else:
        print(f"Sorry, there are no jokes on {joke}, Please try something else")
except:
    print("Sorry, Please try again later...")