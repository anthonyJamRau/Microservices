import requests

# URL of your local Flask app
url = "http://24.199.74.10:5000/todo"

# Example of a POST request to create a to-do item
def create_todo():
    todo_data = {
        "Title": "Buy Groceries",
        "Description": "Need to buy groceries for dinner",
        "DueDate": "2023-10-30",
        "UserId": 1
    }
    
    response = requests.post(url, json=todo_data)
    
    # Print response from the server
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

# Example of a GET request to retrieve the to-do list
def list_todos():
    response = requests.get(url)
    
    # Print response from the server
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

# Example of a PUT request to update an existing to-do item
def update_todo(item_id):
    todo_data = {
        "Title": "Buy Vegetables",
        "Description": "Need to buy vegetables instead",
        "DueDate": "2023-10-31"
    }
    
    response = requests.put(f"{url}/{item_id}", json=todo_data)
    
    # Print response from the server
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

# Example of a DELETE request to delete a to-do item
def delete_todo(item_id):
    response = requests.delete(f"{url}/{item_id}")
    
    # Print response from the server
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

# Test the functions
if __name__ == "__main__":
    # Uncomment one function at a time to test

    # create_todo()  # Create a new to-do item
    # list_todos()   # List all to-do items
    update_todo(1) # Update the to-do item with ID 1
    # delete_todo(1) # Delete the to-do item with ID 1
