import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize the app with the service account key
cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://real-time--face-attendance-default-rtdb.firebaseio.com/"
})

# Create a reference to the "Student" node in the database
ref = db.reference('Students')

# Define student data as a Python dictionary
data = {
"321654":
        {
            "name": "Padmesh Tiwari",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

}

# Loop through the data and add it to the database
for key, value in data.items():
    # Create a child node with the key as the name of the child node and the value as the data
    ref.child(key).set(value)
