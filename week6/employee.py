import json
employee_data = {
    "John Doe": {"salary": 50000, "personal_details": {"age": 30, "department": "Engineering"}},
    "Jane Smith": {"salary": 60000, "personal_details": {"age": 25, "department": "Marketing"}},
    "Alice Johnson": {"salary": 55000, "personal_details": {"age": 28, "department": "Sales"}},
    "Bob Brown": {"salary": 70000, "personal_details": {"age": 35, "department": "HR"}},
    "Max": {"salary": 70000, "personal_details": {"age": 32, "department": "CEO"}}
}
authorised_employee = {
    "Bob Brown":1234,
    "Max":5678
}

def login_required(func):
    def wrapper():
        name = input("Please type your name to Login:")
        passwd = int(input("Please type your password:"))
        if name in authorised_employee and authorised_employee[name] == passwd:
            print(f"Welcome, {name}!")
            return func()
        else:
            print("Access denied.")
    return wrapper

@login_required
def view_salary():
    print("View all Salary")
    for employee, details in employee_data.items():
        print(f"{employee}: ${details['salary']}")

@login_required
def view_personal_details():
    print("View all personal Details")
    for employee, details in employee_data.items():
        print(f"{employee}: Age - {details['personal_details']['age']}, Department - {details['personal_details']['department']}")

@login_required
def download_report():
    with open("report.txt", "w", encoding="utf-8") as f:
        json.dump(employee_data, f, ensure_ascii=False, indent=4)
    print("Downloading report...")


def main():
    while True:
            print("\n==== Employee Management System ====")
            print("1. View Salary")
            print("2. View Personal Details")
            print("3. Download Report")
            print("4. Exit")
    
            choice = input("Select an option (1-4): ")
            if choice == '1':
                view_salary()
            elif choice == '2':
                view_personal_details()
            elif choice == '3': 
                download_report()
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break

if __name__ == "__main__":
    main()

