from database.db import Database
from database.cars_db import CarsDB
from controllers.cars_controller import CarsController
from views.view import View


class MainController:
    
    def __init__(self, db: Database, view: View) -> None:
        self.db = db
        self.cars_db = CarsDB(db)
        self.view = view
        
    def run(self) -> None:
        while True:
            choice = self.view.display_menu(
                "Main Menu",
                {
                    "1": "Manage Cars",
                    "0": "Exit"
                }
            )
            
            if choice == "1":
                cars_controller = CarsController(self.cars_db, self.view)
                cars_controller.run()
            elif choice == "0":
                self.view.display_message("Exiting the application. Goodbye!")
                break
            else:
                self.view.display_message("Invalid choice. Please try again.")