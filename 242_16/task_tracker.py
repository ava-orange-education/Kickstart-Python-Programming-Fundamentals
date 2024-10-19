from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('localhost', 27017)
db = client['task_tracker']
tasks_collection = db['tasks']

# Function to add a new task
def add_task(name, description, due_date, status="Pending"):
    task = {
        "name": name,
        "description": description,
        "due_date": due_date,
        "status": status
    }
    tasks_collection.insert_one(task)

# Function to update a task's status
def update_task_status(task_name, status):
    tasks_collection.update_one(
        {"name": task_name},
        {"$set": {"status": status}}
    )

# Function to retrieve all tasks due by a certain date
def get_tasks_due_by(due_date):
    return tasks_collection.find({"due_date": {"$lte": due_date}})

# Function to delete completed tasks
def delete_completed_tasks():
    tasks_collection.delete_many({"status": "Completed"})

# Example usage
add_task("Finish project", "Complete the final project deliverables", "2023-08-31")
add_task("Prepare presentation", "Prepare slides for the client meeting", "2023-09-01", "In Progress")
update_task_status("Finish project", "Completed")
tasks_due = get_tasks_due_by("2023-09-01")
for task in tasks_due:
    print(task)
delete_completed_tasks()

# Close the connection
client.close()
