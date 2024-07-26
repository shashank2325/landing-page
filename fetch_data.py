import os
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)     # Show all rows (you can adjust this as needed)
pd.set_option('display.width', None)  

# Set the path to your service account key file
cred_path = "key.json"

# Initialize Firebase
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Fetch data from the "messages" collection
messages_ref = db.collection('messages')
docs = messages_ref.stream()

# Prepare data for saving
data = []

for doc in docs:
    doc_dict = doc.to_dict()
    doc_dict['id'] = doc.id  # Add document ID to the data
    data.append(doc_dict)

# Convert data to DataFrame
df = pd.DataFrame(data)

print(df)
