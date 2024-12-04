from database.db import Database
from models.car import Car
from typing import List

class CarsDB:
    
    def __init__(self, db:Database) -> None:
        self.db = db
    
    def insert_car(self, car: Car) -> None:
        query = """INSERT INTO cars(make,model,year)
        VALUES(?,?,?);"""
        self.db.execute_query(query, (car.make, car.model, car.year))
    
    def fetch_all_cars(self) -> List[Car]:
        query = "SELECT * FROM Cars;"
        rows = self.db.fetch_all(query)
        return [Car(row["make"], row["model"], row["year"], row["car_id"]) for row in rows]
    
    def delete_by_id(self, car_id: int) -> None:
        query = "DELETE FROM cars WHERE car_id = ?;"
        self.db.execute_query(query, (car_id,))