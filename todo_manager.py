import pandas as pd
import os

EXCEL_FILE = "todolist.xlsx"

def initialize_database():
    """Create the Excel file if it doesn't exist."""
    if not os.path.exists(EXCEL_FILE):
        df = pd.DataFrame(columns=["ID", "Task", "Category", "Priority", "Status"])
        df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")
        print("Database initialized.")

def load_tasks():
    """Read tasks from the Excel file."""
    initialize_database()
    return pd.read_excel(EXCEL_FILE, engine="openpyxl")

def save_tasks(df):
    """Save the current DataFrame to Excel."""
    df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")

def add_task(df):
    """Add a new task to the list."""
    task_name = input("Enter Task: ").strip()
    category = input("Category (Work/Personal/etc.): ").strip()
    priority = input("Priority (High/Medium/Low): ").strip()
    
    new_id = 1 if df.empty else df["ID"].max() + 1
    new_row = {
        "ID": new_id,
        "Task": task_name,
        "Category": category,
        "Priority": priority,
        "Status": "Pending"
    }
    
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_tasks(df)
    print("Task added successfully!")
    return df

def list_tasks(df):
    """Display all tasks."""
    if df.empty:
        print("\nYour To-Do list is empty.")
    else:
        print("\n" + "="*60)
        print(df.to_string(index=False))
        print("="*60)

def delete_task(df):
    """Remove a task by its ID."""
    list_tasks(df)
    try:
        task_id = int(input("Enter Task ID to delete: "))
        if task_id in df["ID"].values:
            df = df[df["ID"] != task_id]
            save_tasks(df)
            print(f"Task {task_id} deleted.")
        else:
            print("ID not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return df

def main():
    tasks_df = load_tasks()
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("0. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            list_tasks(tasks_df)
        elif choice == "2":
            tasks_df = add_task(tasks_df)
        elif choice == "3":
            tasks_df = delete_task(tasks_df)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()