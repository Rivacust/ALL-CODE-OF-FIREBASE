Initialize Firebase:

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


Create Parent-Child Tree:

# Define the tree structure
tree_structure = {
    'parent1': {
        'child1': {
            'name': 'Alice',
            'age': 5
        },
        'child2': {
            'name': 'Bob',
            'age': 8
        }
    },
    'parent2': {
        'child1': {
            'name': 'Charlie',
            'age': 7
        },
        'child2': {
            'name': 'David',
            'age': 10
        }
    }
}

# Set the tree structure in the database
db.child('family_tree').set(tree_structure)

print("Parent-child tree created successfully")



#db.child is use for parent child relationship
