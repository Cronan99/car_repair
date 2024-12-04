from models.base import BaseModel


class Car(BaseModel):
    def __init__(self, make: str, model: str, year: int, car_id: int = None) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.car_id = car_id