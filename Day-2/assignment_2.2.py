import pandas as pd

# Create a dataset with messy data
data = {
    "Name": ["  JOHN123 ", "Alice@45", "  Bob!! ", "Emma#99"],
    "Email": [
        " JOHN@GMAIL.COM ",
        "alice@GMAIL.COM",
        "bob123@yahoo.com",
        "emma#@gmail.com"
    ],
    "Phone": ["987-654-3210", "123 456 7890", "987@654@3210", "456.789.1230"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Clean Name: remove numbers and special characters
df["Name"] = df["Name"].str.replace(r"[^a-zA-Z\s]", "", regex=True).str.strip()

# Clean Email: convert to lowercase and remove spaces
df["Email"] = df["Email"].str.lower().str.strip()

# Clean Phone: keep only digits
df["Phone"] = df["Phone"].str.replace(r"\D", "", regex=True)

print("\nCleaned Data:")
print(df)