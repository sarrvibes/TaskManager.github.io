from models.operasi import TaskManager
from manage.Menu import main_menu

if __name__ == "__main__":
    tasks = TaskManager()
    main_menu(tasks)
