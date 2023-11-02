# ZEVO Rental Application User Guide

Welcome to ZEVO, the electric vehicle rental application! Whether you are a customer, operator, or manager, this user guide will help you get the most out of our platform. ZEVO offers a convenient and eco-friendly solution for renting electric vehicles, including e-bikes and e-cars. ZEVO stands for Zero(Z-O) Emission Electric Vehicles(EV) 

Let's get started:

## Table of Contents

- [ZEVO Rental Application User Guide](#zevo-rental-application-user-guide)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Development](#development)
    - [Creating an Account](#creating-an-account)
    - [Logging In](#logging-in)
  - [Features](#features)
    - [For Customers](#for-customers)
    - [For Operators](#for-operators)
    - [For Managers](#for-managers)
  - [Using ZEVO](#using-zevo)
    - [Navigating the App](#navigating-the-app)
    - [Customer Features](#customer-features)
    - [Operator Features](#operator-features)
    - [Manager Features](#manager-features)
  - [Reporting and Support](#reporting-and-support)

## Getting Started

### Prerequisites

Before you start using ZEVO, make sure you have the following:

- A compatible computer with internet access.
- A ZEVO user account (customer, operator, or manager).
- The ZEVO mobile app or access to the web-based application.

### Development
- Requirements:
  - Python 3.10+
  - Any code editor, eg. VSCode, Atom
  - Pip 22.0+ (Run ```py -m ensurepip --upgrade``` to install pip)
  - Poetry 1.6.0+ (Run ```pip install poetry```)

- Setup steps
  - After the requirements are satisfied, open a terminal on the project root directory.
  - Run ```poetry install``` to install the project dependencies
  
- Running the application
  - Run ```python main.py``` or ```py -m main.py``` to run the project

- Sample user credentials for different user groups
  - User (Customer)
      - email: mahesh@zevo.com
      - password: xyz123
  - Operator
    - email: ju@zevo.com
    - password: xyz123
  - Manager
    - email: li@zevo.com
    - password: xyz123


### Creating an Account

If you're new to ZEVO, you'll need to create an account:

1. *Sign up on the App*: Fill in the details on the signup page and the hit register, log back in with the credentials you typed in

### Logging In

If you already have a ZEVO account, follow these steps to log in:

1. Open the ZEVO app on your device.

2. Select "Log In."

3. Enter your email and password.

4. Click "Log In."

Now that you're logged in, let's explore the features available based on your role.

## Features

ZEVO offers distinct features for different user roles: customers, operators, and managers.

### For Customers

As a customer, you can enjoy the following features:

- *Searching for Vehicles by Locations:* Customers can easily search for electric cars and e-bikes located near them, making it convenient to find the perfect vehicle for their needs.

- *View Vehicle Information:* Customers can access vital information about available vehicles, including details such as range, price, current energy (battery charge), number of doors, model, brand, color, number of seats, and more. This feature ensures that customers have all the necessary information to make an informed choice.

- *Renting a Vehicle:* Customers can rent an available vehicle and use it for a duration, providing them with flexibility and freedom to travel as they desire.

- *Returning a Vehicle:* When customers are done with their rental, they can return the vehicle to any of our drop locations and pay for the total service amount, ensuring a hassle-free and straightforward process.

- *Reporting Vehicle Issues:* In the event a customer encounters a malfunctioning or damaged vehicle, they can easily report the issue through the application, helping us maintain the quality and safety of our fleet.

### For Operators

Operators have access to features designed to manage and maintain the ZEVO fleet:

- *Track Vehicle Locations:* Monitor the locations of all ZEVO vehicles in the city.

- *Charge Depleted Vehicles:* Initiate the charging process when a vehicle's battery is depleted.

- *Repair Defective Vehicles:* Request repair services for malfunctioning vehicles or reported defects.

- *Relocate Vehicles:* Move vehicles to different locations in the city as needed.

### For Managers

Managers have reporting and data visualization tools to optimize the service:

- *Generate Reports:* Create detailed reports showing all vehicle activities over a specified time period, using data visualization techniques to make informed decisions.

## Using ZEVO

### Navigating the App

ZEVO's user-friendly interface makes navigation easy:

- *Welcome:* This is the first screen on the application and leads the user to the login and Sign up.

- *User groups* There are three user groups in the app, 'user', 'manager' and 'operator'. Based on the user role, the pages load. For example, if an operator logs in, it opens the 'Operator dashboard'.
  
- *Navigation Bar* A navigation bar appears on the Vehicles List (Home) page and 'Purchase history' pages. Using this bar, the user can navigate between Home Page, Purchase History page or Log out of the application.
- *Back arrow* Users can return to the previous page by clicking on the back arrow button on relevant pages

### Customer Features

For customers, ZEVO offers the following features:

- *Locate Vehicles:* Use the location selector function to find vehicles near your preferred location.

- *View Details:* Click on a vehicle to access information like range, price, and more.

- *Rent a Vehicle:* Rent a vehicle for your desired duration.

- *Return:* Return the vehicle to any ZEVO office and complete the payment.

- *Report Issues:* Report any problems with a vehicle.

### Operator Features

Operators can manage ZEVO vehicles efficiently:

- *Monitor Locations:* Use the app to track the real-time locations of vehicles.

- *Charge Vehicles:* Start the charging process for depleted vehicles.

- *Request Repairs:* Report and request repairs for malfunctioning vehicles.

- *Relocate Vehicles:* Move vehicles to optimize availability and accessibility.

### Manager Features

Managers benefit from advanced data analysis tools:

- *Generate Reports:* Create comprehensive reports on vehicle activities over specific time periods.

- *Data Visualization:* Use data visualization techniques to make data-driven decisions and optimize the service.

## Reporting and Support

If you have any questions, need assistance, or want to report an issue, contact our support team at [support@zevo.com](mailto:support@zevo.com). We are here to help you make the most of your ZEVO experience.

Thank you for choosing ZEVO for your electric vehicle rental needs! Enjoy eco-friendly and convenient transportation with us.

Drive Green, Drive ZEVO