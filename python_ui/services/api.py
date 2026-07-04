import requests

url = "http://127.0.0.1:8000"
def SendData(title:str):
    res = requests.post(f"{url}/add_todo", json={"title":title})

    if res.content:
        return res.json()
    else:
        return {"error":"Post Sending Error"}
    
def all_Todo():
    res = requests.get(f"{url}/all_todo")
    if res:
        return res.json()
    else:
        return {"error":"Soming went wrong"}

def delete_todo(id:int):
    res = requests.delete(f"{url}/delete_todo/{id}")
    if res:
        return res.json()
    else:
        return {"error":"Something went wrong"}
    
def edit_todo(id:int, title:str):
    res = requests.put(f"{url}/update_todo/{id}", params={"text":title})
    if res:
        return res.json()
    else:
        return {"error":"Something went wrong"}
    
def complete_todo(id:int): 
    res = requests.put(f"{url}/complete/{id}")
    if res:
        return res.json()
    else:
        return {"error":"Something went wrong"}    