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
                [type] TEXT,
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
                [defects] TEXT
                  )
                ''')

        self.c.execute('''
                CREATE TABLE IF NOT EXISTS users
                ([userid], integer PRIMARY KEY,
                [username] TEXT,
                [email] TEXT,
                [secret] TEXT,
                [usertype] TEXT)
                ''')
        self.conn.commit()
        if self.validate_new_db() == True:
            print("Db is empty")
            self.populate_mock_data()
        # self.root.mainloop()
        # self.welcomeScreen = welcome()

    # Methods
    def populate_mock_data(self):
        print("populating mock data in the database...")
        self.c.execute('''
                    INSERT INTO vehicles (type, make, model, licensePlateNumber, ratePerWeek, ratePerDay, ratePerHour, batteryCapacity, range, doors, seatingCapacity, horsePower, maxSpeed, inUse, atSite, history, defects)
                    VALUES
                    ('Sedan', 'Toyota', 'Camry', 'ABC123', 200, 40, 5, 60000, 450, 4, 5, 180, 130, 0, 1, 'History for Camry', 'No defects'),
                    ('SUV', 'Honda', 'CR-V', 'XYZ789', 250, 50, 6, 70000, 400, 5, 5, 200, 140, 0, 1, 'History for CR-V', 'Minor scratches'),
                    ('Electric', 'Tesla', 'Model 3', 'EV456', 300, 60, 10, 80000, 300, 4, 5, 250, 150, 1, 0, 'History for Model 3', 'Battery issue');
        ''')

        self.c.execute('''INSERT INTO users (username, email, secret, usertype)
            VALUES
            ('Mahesh', 'mahesh@zevo.com', 'xyz123', 'user');
            ''')
        self.c.execute('''INSERT INTO users (username, email, secret, usertype)
            VALUES
            ('Ju', 'ju@zevo.com', 'xyz123', 'operator');
            ''')
        self.c.execute('''INSERT INTO users (username, email, secret, usertype)
            VALUES
            ('Li', 'mahesh@zevo.com', 'xyz123', 'manager');
            ''')

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
        print("All vehicles: ", df)
