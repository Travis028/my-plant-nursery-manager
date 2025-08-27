# database

import sqlite3

class Databaseconnction:
    def __init__(self, host):
        self.connection = None
        self.host = host
        pass