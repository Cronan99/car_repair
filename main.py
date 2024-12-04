from database.db import Database
from controllers.main_controller import MainController
from views.view import View


def main():
    db = Database()
    db.connect()
    db.setup_tables()
    
    view = View()
    
    app_controller = MainController(db, view)
    app_controller.run()
    
    db.close()
    
if __name__ =="__main__":
    main()