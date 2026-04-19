import requests
import pandas as pd

URL = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-nonfiction.json"
params = {"api-key" : "INSERT_YOUR_KEY_HERE"}

response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()
else:
    print("Error, unable to retrieve data.")

best_sellers = data["results"]["books"]
dataframe_1 = pd.DataFrame(best_sellers)
dataframe_1 = dataframe_1[["title", "author", "publisher", "rank"]]
print(dataframe_1)
