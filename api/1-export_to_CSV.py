import requests
import csv
import sys

def get_employee_todo_progress(employee_id):
    # API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    try:
        # Fetch employee details
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data["name"]

        # Fetch TODO list
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        done_tasks = sum(1 for task in todos_data if task["completed"])

        # Create CSV file
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode="w", newline="") as csvfile:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for task in todos_data:
                writer.writerow({
                    "USER_ID": employee_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": "Completed" if task["completed"] else "Not Completed",
                    "TASK_TITLE": task["title"]
                })

        print(f"CSV file '{csv_filename}' created successfully!")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)