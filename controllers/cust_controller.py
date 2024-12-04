from models.customer import Customer
from database.cust_db import CustDB
from views.view import View


class CustomerController:
    
    def __init__(self, cust_db: CustDB, view: View) -> None:
        self.cust_db = cust_db
        self.view = view
        
    def run(self) -> None:
        while True:
            choice = self.view.display_menu("Customer Management",
                {
                    "1": "Add Customer",
                    "2": "View All Customers",
                    "3": "Delete Customer",
                    "0": "Back to Main Menu"   
                }                        
            )
            
            if choice == "1":
                self.add_customer()
            elif choice == "2":
                self.view_all_customers()
            elif choice == "3":
                self.delete_customer()
            elif choice == "0":
                break
            else:
                self.view.display_message("Invalid choice. Please try again.")
                
    def add_customer(self) -> None:
        first_name = self.view.get_input("Enter First Name: ")
        if not first_name or first_name is None:
            self.view.display_message("First Name cannot be empty or None!")
            return 
               
        last_name = self.view.get_input("Enter Last Name: ")
        if not last_name or last_name is None:
            self.view.display_message("Last Name cannot be empty or None!")
            return
        
        cust = Customer(first_name, last_name)
        self.cust_db.insert_customer(cust)
        self.view.display_message("Customer added successfully.")
        
    def view_all_customers(self) -> None:
        cust = self.cust_db.fetch_all_customers()
        self.view.display_items(cust)
        
    def delete_customer(self) -> None:
        cust_id = self.view.get_int_input("Enter the cust_id to delete:")
        self.cust_db.delete_by_id(cust_id)
        self.view.display_message("Customer deleted successfully.")
