import requests as rq
res = rq.get("http://www.tutoreye.com")
print(res)
print(res.ok)
print(res.headers)
print(res.text)
newres = rq.get("http://icanhazdadjoke.com",headers={"Accept":"text/plain"})
print(newres.text)
#to find json data you can use application/json
res2 = rq.get("http://icanhazdadjoke.com",headers={"Accept":"application/json"})
print(res2.text)
print(res2.json())
#res.json() returns a dictionary