import requests as rq
res = rq.get("http://icanhazdadjoke.com/search",
              headers={"Accept":"application/json"},
              params={"term":"dog"}
                       )
print(res.json())