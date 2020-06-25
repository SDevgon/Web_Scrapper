import requests
import json
suma=0.0
r = requests.get("http://py4e-data.dr-chuck.net/comments_628958.json")
print(r)
#res = json.loads(r)
#print(res)
res=r.json()  #dictionary created
#print(type(res.get("comments")))
for i in res.get("comments"):
    suma+=float(i.get("count"))   

print(float(suma))