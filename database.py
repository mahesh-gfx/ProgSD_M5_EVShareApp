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

        self.c.execute('''
                CREATE TABLE IF NOT EXISTS orders
                ([orderid] INTEGER PRIMARY KEY,
                [username] TEXT,
                [startTime] TEXT,
                [endTime] TEXT,
                [income] TEXT)
                ''')
        self.c.execute('''
                CREATE TABLE IF NOT EXISTS payments
                ([email] TEXT PRIMARY KEY,
                [cardnum] TEXT,
                [cardname] TEXT,
                [expire] TEXT,
                [CVV] TEXT,
                [credits] INTEGER);
                ''')
        self.c.execute('''
                CREATE TABLE IF NOT EXISTS discounts
                ([code] TEXT PRIMARY KEY,
                [amount] INTEGER);
                ''')

        self.conn.commit()
        if self.validate_new_db() == True:
            print("Db is empty")
            self.populate_mock_data()
    
    def insert_payments(self, email, cardnum, cardname, expire, CVV, credits):
        print("Insert "+str(email) + "payment inform...")
        self.c.execute("SELECT * FROM payments WHERE email = ?", (email,))
        payment = self.c.fetchone()
        if payment:
            current_credits = payment[5]+credits
            cardnums = payment[1].split()
            if cardnum not in cardnums:
                current_cardnum = payment[1]+(" "+str(cardnum))
                current_cardname = payment[2]+(" "+str(cardname))
                current_expire = payment[3]+(" "+str(expire))
                current_CVV = payment[4]+(" "+str(CVV))
            self.c.execute('''UPDATE payments
                          SET cardnum = ?, cardname = ?, expire = ?, CVV = ?, credits = ?
                          WHERE email = ?''', (current_cardnum,current_cardname,current_expire,current_CVV,current_credits, email))
        else:
            self.c.execute('''INSERT INTO payments (email, cardnum, cardname, expire, CVV, credits)
                             VALUES (?, ?, ?, ?, ?, ?)''', [email, cardnum, cardname, expire, CVV, credits])
        self.conn.commit()

    def insert_discount(self):
        print("Insert 3 discounts...")
        code = ['FALL2023','WINTER2023','NEWAPP']
        amount = [5,6,10]
        for i in range(len(code)):
            self.c.execute('''INSERT INTO discounts (code, amount)
                             VALUES (?, ?)''', [code[i],amount[i]])
        self.conn.commit()
        

    def insert_tesla_vehicles(self, num_vehicles=3100):
        import random
        import datetime
        defects = ['Can\'t connect bluetooth', 'Wrong battery status',
                   'Type problems', 'Traffic accident', 'fine']
        one_month_ago = datetime.datetime.now() - datetime.timedelta(days=30)

        # 车辆类型选择列表，包括电动车和电动自行车
        vehicle_types = ['Electric', 'Electric Bike']

        for _ in range(num_vehicles):
            # 随机生成一些示例数据，可以根据需要进行修改
            type = random.choice(vehicle_types)  # 随机选择车辆类型
            make = 'Tesla'  # 制造商
            if type == 'Electric':
                model = random.choice(
                    ['Model 3', 'Model S', 'Model X', 'Model Y'])  # 随机选择特斯拉的车型
                # 针对电动车类型进行特殊处理
                ratePerWeek = random.randint(100, 300)  # 随机生成每周租金费用
                ratePerDay = random.randint(20, 60)  # 随机生成每日租金费用
                ratePerHour = random.randint(5, 20)  # 随机生成每小时租金费用
                batteryCapacity = random.randint(50000, 80000)  # 随机生成电池容量
                range1 = random.randint(300, 500)  # 随机生成续航里程
                doors = random.randint(2, 5)  # 随机生成门数
                seatingCapacity = random.randint(2, 7)  # 随机生成座位容量
                horsePower = random.randint(100, 400)  # 随机生成马力
                maxSpeed = random.randint(100, 200)  # 随机生成最高速度
            else:
                model = random.choice(
                    ['E-Bike Model A', 'E-Bike Model B', 'E-Bike Model C'])  # 电动自行车的车型
                # 电动自行车特殊处理
                ratePerWeek = random.randint(20, 60)  # 80% 减少租金费用
                ratePerDay = random.randint(4, 12)  # 80% 减少租金费用
                ratePerHour = random.randint(1, 4)  # 80% 减少租金费用
                batteryCapacity = random.randint(0, 10000)  # 0 到 10000 电池容量
                range1 = random.randint(10, 30)  # 10 到 30 续航里程
                doors = 0  # 电动自行车没有门
                seatingCapacity = 1  # 电动自行车的座位容量
                horsePower = 0  # 电动自行车没有马力
                maxSpeed = random.randint(10, 15)  # 1 到 15 最高速度

            licensePlateNumber = ''.join(random.choices(
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=7))  # 随机生成车牌号
            inUse = random.randint(0, 1)  # 随机生成是否在使用
            atSite = random.randint(0, 1)  # 随机生成是否在站点
            history = 'History for ' + model  # 车辆历史信息
            # 生成随机时间戳从现在到一个月前
            defect_time = (one_month_ago + datetime.timedelta(days=random.randint(1, 30))).strftime(
                "%Y-%m-%d %H:%M:%S")
            defect = random.choice(defects) + ',' + defect_time

            # 使用参数化查询将数据插入到数据库中
            self.c.execute('''
                    INSERT INTO vehicles (type, make, model, licensePlateNumber, ratePerWeek, ratePerDay, ratePerHour, batteryCapacity, range, doors, seatingCapacity, horsePower, maxSpeed, inUse, atSite, history, defects)
                    VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                type, make, model, licensePlateNumber, ratePerWeek, ratePerDay, ratePerHour, batteryCapacity, range1,
                doors, seatingCapacity, horsePower, maxSpeed, inUse, atSite, history, defect))
            self.conn.commit()
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
        query = 'SELECT * FROM vehicles '
        vehicles = self.run_query(query)
        df = pd.DataFrame(vehicles.fetchall(), columns=[
                          'vehicle_id', 'type'])
        # print("All vehicles: ", df)

if __name__ == '__main__':
    db = db()
    db.insert_discount()
    db.insert_payments('mahesh@zevo.com', "","","","",1000)
    db.insert_payments('mahesh@zevo.com', "11111","1","111","1",10)