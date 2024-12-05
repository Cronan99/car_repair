import sqlite3
from typing import Optional


class Database:

    def __init__(self, db_name: str = "car_repair_manager.db") -> None:
        self.db_name = db_name
        self.connection: Optional[sqlite3.Connection] = None

    def connect(self) -> None:
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)
            self.connection.row_factory = sqlite3.Row

    def close(self) -> None:
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query: str, params: tuple=()) -> None:
        if not self.connection:
            raise RuntimeError("Database not connected")
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query: str, params: tuple=()) -> list[sqlite3.Row]:
        if not self.connection:
            raise RuntimeError("Database not connected")
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def fetch_one(self, query: str, params: tuple=()) -> Optional[sqlite3.Row]:
        if not self.connection:
            raise RuntimeError("Database not connected")
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

    def setup_tables(self) -> None:
        car_table = """
        CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL
        );
        """

        customer_table = """
        CREATE TABLE IF NOT EXISTS customer (
            cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT  NOT NULL
        );
        """
        
        #Fixa så att SQL fungerar för reparation
        reparation_table = """
        CREATE TABLE IF NOT EXISTS repair (
            repair_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cust_id INTEGER,
            car_id INTEGER,
            FOREIGN KEY (cust_id) REFERENCES customer(cust_id),
            FOREIGN KEY (car_id) REFERENCES cars(car_id)
        );
        """
        self.execute_query(reparation_table)
        self.execute_query(car_table)
        self.execute_query(customer_table)