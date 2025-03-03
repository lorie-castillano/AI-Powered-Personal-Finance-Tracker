from celery import Celery

app = Celery('tasks', broker='redis://redis:6379/0')

@app.task
def categorize_expense(expense_data):
    # ML categorization logic here
    return {"category": "food"}
