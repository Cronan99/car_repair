from models.base import BaseModel

class Customer(BaseModel):
    def __init__(self, first_name: str, last_name: str, cust_id: int = None) -> None:
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name