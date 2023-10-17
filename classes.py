import datetime


class vehicleHistory:
    user = ""
    startTime = ""
    endTime = ""
    site = ""
    distance = ""
    battery = ""
    paymentStatus = ""
    paymentId = ""

    def __init__(self, user="admin", startTime=datetime.datetime.now(), endTime=datetime.datetime.now(), distance="0", battery="0", site="HQ"):
        self.user = user
        self.startTime = startTime
        self.endTime = endTime
        self.site = site
        self.distance = distance
        self.battery = battery


defaultHistory = vehicleHistory(
    user='admin', startTime=datetime.datetime.now(), endTime=datetime.datetime.now(), site='hq', distance="0", battery='10')


class defects:
    defect = ""
    severity = ""
    reportedBy = ""
    reportedOn = ""
    fixed = False
    fixedOn = ""
    fixedBy = ""
    fixedAt = "site"

    def __init__(self, defect="",
                 severity="ukwn",
                 reportedBy="admin",
                 reportedOn=datetime.datetime.now(),
                 fixed=False,
                 fixedOn="",
                 fixedBy="",
                 fixedAt="site"):
        self.defect = defect
        self.severity = severity
        self.reportedBy = reportedBy
        self.reportedOn = reportedOn
        self.fixed = fixed
        self.fixedOn = fixedOn
        self.fixedBy = fixedBy
        self.fixedAt = fixedAt


defaultDefect = defects(defect='None')


class Vehicle:
    type = ""
    vehicleClass = ""
    make = ""
    model = ""
    licensePlateNumber = ""
    ratePerWeek = ""
    ratePerDay = ""
    ratePerHour = ""
    batteryCapacity = ""
    range = ""
    doors = ""
    seatingCapacity = ""
    horsepower = ""
    maxSpeed = ""

    # Status
    inUse = False
    atSite = True

    history = []
    defects = []

    def __init__(self, type, vehicleClass, make,
                 model,
                 licensePlateNumber,
                 ratePerWeek="20",
                 ratePerDay="3.5",
                 ratePerHour="0.2",
                 batteryCapacity="5kWh",
                 range="50",
                 doors="0",
                 seatingCapacity="1",
                 horsepower="1",
                 maxSpeed="25",
                 inUse=False,
                 atSite=True,
                 ):
        self.type = type
        self.vehicleClass = vehicleClass
        self.licensePlateNumber = licensePlateNumber
        self.ratePerWeek = ratePerWeek
        self.ratePerDay = ratePerDay
        self.ratePerHour = ratePerHour
        self.batteryCapacity = batteryCapacity
        self.range = range
        self.doors = doors
        self.seatingCapacity = seatingCapacity
        self.horsepower = horsepower
        self.maxSpeed = maxSpeed
        self.inUse = inUse
        self.atSite = atSite
        self.history = [defaultHistory]
        self.defects = [defaultDefect]


class user:
    username = ''
    email = ''
    secret = ''
    purchaseHistory = []

    def __init__(self, username, email, secret):
        print('creating user...')
        self.username = username
        self.email = email
        self.secret = secret
