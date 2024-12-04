from database.db import Database
from models.customer import Customer
from typing import List

class CustDB:

    def __init__(self, db: Database) -> None:
        self.db = db
    
    def insert_customer(self, customer: Customer):
        query = """INSERT INTO customer(first_name,last_name)
        VALUES(?,?);"""
        self.db.execute_query(query, (customer.first_name, customer.last_name))

    def fetch_all_customers(self) -> List[Customer]:
        query = "SELECT * FROM customer;"
        rows = self.db.fetch_all(query)
        return [Customer(row["first_name"], row["last_name"], row["cust_id"]) for row in rows]

    def delete_by_id(self, cust_id: int) -> None:
        query = "DELETE FROM customer WHERE cust_id = ?;"
        self.db.execute_query(query, (cust_id,))