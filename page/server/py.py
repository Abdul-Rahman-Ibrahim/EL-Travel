import requests
import pandas as pd
response = requests.get("../passport_form.html")
print(response.status_code)
print(response.json())
res = pd.DataFrame(response.json()["people"])
res.head()
