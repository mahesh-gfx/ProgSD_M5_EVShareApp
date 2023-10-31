import sqlite3
import pandas as pd


class db():
    def __init__(self):
        print("Initializing database...")
        self.conn = sqlite3.connect('zevo-dev.db')
        self.c = self.conn.cursor()

        self.c.execute('''
                CREATE TABLE IF NOT EXISTS vehicles
                ([vehicle_id] INTEGER PRIMARY KEY,
                [vehicleClass] TEXT,
                [make] TEXT,
                [model] TEXT,
                [licensePlateNumber] TEXT,
                [ratePerWeek] INTEGER,
                [ratePerDay] INTEGER,
                [ratePerHour] INTEGER,
                [batteryCapacity] INTEGER,
                [range] INTEGER,
                [doors] INTEGER,
                [seatingCapacity] INTEGER,
                [horsePower] INTEGER,
                [maxSpeed] INTEGER,
                [inUse] BOOLEAN,
                [atSite] BOOLEAN,
                [history] TEXT,
                [defects] TEXT,
                [image] TEXT,
                [bg] TEXT,
                [fg] TEXT,
                [location] TEXT,
                [hasDefects] BOOLEAN       
                       );
                ''')

        self.c.execute('''
                CREATE TABLE IF NOT EXISTS users
                ([userid] INTEGER PRIMARY KEY,
                [username] TEXT,
                [email] TEXT,
                [secret] TEXT,
                [usertype] TEXT,
                [purchase] TEXT);
                ''')
        self.conn.commit()
        if self.validate_new_db() == True:
            print("Db is empty")
            self.populate_mock_data()

    # Methods
    def populate_mock_data(self):
        print("populating mock data in the database...")

        vehicles = [
            {
                "type": "Car",
                "vehicleClass": "SUV",
                "make": "Tesla",
                "model": "Model S",
                "licensePlateNumber": "XYZ 123",
                "ratePerWeek": 20,
                "ratePerDay": 4,
                "ratePerHour": 0.2,
                "batteryCapacity": "64kWh",
                "range": 550,
                "doors": 5,
                "seatingCapacity": 7,
                "horsePower": 200,
                "maxSpeed": 310,
                "inUse": 0,  # False is represented as 0 in SQLite
                "atSite": 1,  # True is represented as 1 in SQLite
                "history": '[]',  # Convert to string
                "defects": '[]',  # Convert to string
                "image": "blue-tesla",
                "bg": "#04317D",
                "fg": "#FFFFFF",
                "location": "0.2",
                "hasDefects": 0
            },
            {
                "type": "Car",
                "vehicleClass": "SUV",
                "make": "Tesla",
                "model": "Model S",
                "licensePlateNumber": "XYZ 123",
                "ratePerWeek": 20,
                "ratePerDay": 4,
                "ratePerHour": 0.2,
                "batteryCapacity": "64kWh",
                "range": 550,
                "doors": 5,
                "seatingCapacity": 7,
                "horsePower": 200,
                "maxSpeed": 310,
                "inUse": 0,
                "atSite": 1,
                "history": '[]',
                "defects": '[]',
                "image": "red-tesla",
                "bg": "#D22739",
                "fg": "#FFFFFF",
                "location": "0.8",
                "hasDefects": 0
            },
            {
                "type": "Car",
                "vehicleClass": "SUV",
                "make": "Tesla",
                "model": "Model S",
                "licensePlateNumber": "XYZ 123",
                "ratePerWeek": 20,
                "ratePerDay": 4,
                "ratePerHour": 0.2,
                "batteryCapacity": "64kWh",
                "range": 550,
                "doors": 5,
                "seatingCapacity": 7,
                "horsePower": 200,
                "maxSpeed": 310,
                "inUse": 0,
                "atSite": 1,
                "history": '[]',
                "defects": '[]',
                "image": "white-tesla",
                "bg": "#ECEDED",
                "fg": "#000000",
                "location": "0.7",
                "hasDefects": 0
            },
        ]

        # Insert vehicles
        for item in vehicles:
            self.c.execute('''INSERT INTO vehicles
                    (vehicleClass, make, model, licensePlateNumber, ratePerWeek, ratePerDay, ratePerHour,
                    batteryCapacity, range, doors, seatingCapacity, horsePower, maxSpeed, inUse, atSite, history, defects, image, bg, fg, location)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                           (item["vehicleClass"], item["make"], item["model"], item["licensePlateNumber"],
                            item["ratePerWeek"], item["ratePerDay"], item["ratePerHour"],
                               item["batteryCapacity"], item["range"], item["doors"], item["seatingCapacity"],
                               item["horsePower"], item["maxSpeed"], item["inUse"], item["atSite"],
                               item["history"], item["defects"], item["image"], item["bg"], item["fg"], item["location"]))

        user_data = [
            ('Mahesh', 'mahesh@zevo.com', 'xyz123', 'user'),
            ('Ju', 'ju@zevo.com', 'xyz123', 'operator'),
            ('Li', 'mahesh@zevo.com', 'xyz123', 'manager')
        ]

        # Insert users
        for data in user_data:
            self.c.execute('''INSERT INTO users (username, email, secret, usertype)
                             VALUES (?, ?, ?, ?)''', data)

        self.conn.commit()

    # check if there are tabled in the database and if they have data
    def validate_new_db(self):
        # Check if the table is empty
        self.c.execute(f"SELECT COUNT(*) FROM vehicles")
        row_count = self.c.fetchone()[0]
        is_empty = row_count == 0
        print("Is database empty? ", is_empty)
        return is_empty

    # Function to Execute Database Queries
    def run_query(self, query, parameters=()):
        result = self.c.execute(query, parameters)
        self.conn.commit()
        return result

    # Get vehicles from Database
    def get_all_vehicles(self):
        query = 'SELECT * FROM vehicles ORDER BY name'
        vehicles = self.run_query(query)
        df = pd.DataFrame(vehicles.fetchall(), columns=[
                          'vehicle_id', 'type'])
        # print("All vehicles: ", df)
