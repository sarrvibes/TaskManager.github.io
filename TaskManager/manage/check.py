from datetime import datetime, timedelta
from models.operasi import TaskManager

def check_deadline(tasks, days_before=2):
    tasks = TaskManager()
    tasks.check_deadline(days_before)
