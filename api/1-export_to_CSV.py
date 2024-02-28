import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data["name"]
        user_id = user_data["id"]

        # Create a CSV file with the employee's ID as the filename
        filename = {user_id}+".csv"
        with open(filename, mode="w", newline="") as csvfile:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for task in todos_data:
                #task_id = task["id"]
                task_title = task["title"]
                task_completed = task["completed"]

                writer.writerow({
                    "USER_ID": user_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": "Completed" if task_completed else "Not Completed",
                    "TASK_TITLE": task_title
                })

        print(f"Data exported to {filename} successfully!")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python script.py <employee_id>")
#         sys.exit(1)

#     employee_id = int(sys.argv[1])
#     get_employee_todo_progress(employee_id)