import requests
import pandas as pd
import os

token = os.getenv("API_TOKEN")
print(f"Token : {token}")

#response=requests.get("https://jsonplaceholder.typicode.com/users")
#data = response.json()
#df = pd.DataFrame(data)
#answer=df[["id","name"]]

#print(answer)
