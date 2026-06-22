import requests
import pandas as pd


url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

df = pd.DataFrame(response.json())

print(df.columns)

df = df[
    ["id", "name", "username", "email", "phone", "website"]
]

# Uppercase names
df["name"] = df["name"].str.upper()

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing emails
df = df.dropna(subset=["email"])

df.to_excel("users.xlsx", index=False)

print("Excel created") 