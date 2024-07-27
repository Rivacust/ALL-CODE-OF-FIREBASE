Insert Data:

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize the app with a service account, granting admin privileges
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://<DATABASE_NAME>.firebaseio.com/'
})

# Reference to the database
ref = db.reference('path/to/data')

# Insert data
ref.set({
    'name': 'John Doe',
    'age': 30
})

print("Data inserted successfully")



DELETE DATA:


import pyrebase

# Firebase config
config = {
    "apiKey": "your-api-key",
    "authDomain": "your-project-id.firebaseapp.com",
    "databaseURL": "https://your-database-name.firebaseio.com",
    "projectId": "your-project-id",
    "storageBucket": "your-project-id.appspot.com",
    "messagingSenderId": "your-messaging-sender-id",
    "appId": "your-app-id"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()
# Delete data
db.child('path/to/data').remove()
print("Data deleted successfully")
