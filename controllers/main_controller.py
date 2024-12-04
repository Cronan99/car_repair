from database.db import Database
from database.cars_db import CarsDB
from database.cust_db import CustDB
from controllers.cars_controller import CarsController
from controllers.cust_controller import CustomerController
from views.view import View


class MainController:
    
    def __init__(self, db: Database, view: View) -> None:
        self.db = db
        self.cars_db = CarsDB(db)
        self.cust_db = CustDB(db)
        self.view = view
        
    def run(self) -> None:
        while True:
            choice = self.view.display_menu(
                "Main Menu",
                {
                    "1": "Manage Cars",
                    "2": "Manage Customers",
                    "0": "Exit"
                }
            )
            
            if choice == "1":
                cars_controller = CarsController(self.cars_db, self.view)
                cars_controller.run()
            elif choice == "2":
                cust_controller = CustomerController(self.cust_db, self.view)
                cust_controller.run()
            elif choice == "0":
                self.view.display_message("Exiting the application. Goodbye!")
                break
            else:
                self.view.display_message("Invalid choice. Please try again.")