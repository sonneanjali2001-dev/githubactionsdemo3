import requests
import pandas as pd

response=requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()
df = pd.DataFrame(data)
answer=df[["id","name"]]

print(answer)