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

# Update data
ref.update({
    'name': 'Jane Doe',
    'age': 32
})

print("Data updated successfully")
