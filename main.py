import tkinter as tk
from screens import welcome
import sqlite3
import pandas as pd
from database import db
from screens.welcome import welcome


class App():
    # Attributes
    vehicles = []
    db_name = 'zevo-dev.db'

    # Constructors
    def __init__(self):
        print("Constructing App...")
        self.database = db()
        self.welcome = welcome()


a = App()
