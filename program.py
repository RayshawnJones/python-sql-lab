import psycopg2
from psycopg2.extras import RealDictCursor

def connect_to_db():
    return psycopg2.connect(database='companies')

def read_employee(cursor):
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    for employee in employees:
        print(employee)

def read_company(cursor):
    cursor.execute("SELECT * FROM companies")
    companies = cursor.fetchall()
    for company in companies:
        print(company)

def create_employee(cursor):
    name = input("Enter Employee Name: ")
    company_id = input("Enter Company ID: ")
    cursor.execute("INSERT INTO employees (name, company_id) VALUES (%s, %s)", (name, company_id))
    print("Employee has been created successfully.")

def create_company(cursor):
    name = input("Enter Company Name: ")
    cursor.execute("INSERT INTO companies (name) VALUES (%s)", (name,))
    print("Company has been created successfully.")

def update_employee(cursor):
    employee_id = input("Enter Employee ID: ")
    new_name = input("Enter Updated Employee Name: ")
    new_company_id = input("Enter Updated Company ID: ")
    cursor.execute("UPDATE employees SET name = %s, company_id = %s WHERE id = %s", (new_name, new_company_id, employee_id))
    print("Employee Updated Successfully.")

def update_company(cursor):
    company_id = input("Enter Company ID: ")
    new_name = input("Enter New Company Name: ")
    cursor.execute("UPDATE companies SET name = %s WHERE id = %s", (new_name, company_id))
    print("Company Updated Successfully.")

def delete_employee(cursor):
    employee_id = input("Enter Employee ID you wish to delete: ")
    cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
    print("Employee Deleted Successfully.")

def delete_company(cursor):
    company_id = input("Enter Company ID you wish to delete: ")
    cursor.execute("DELETE FROM companies WHERE id = %s", (company_id,))
    print("Company Deleted Successfully.")

def main():
    with connect_to_db() as connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            while True:
                print('CRM MENU')
                print('1. Create Employee')
                print('2. Create Company')
                print('3. Read Employee')
                print('4. Read Company')
                print('5. Update Employee')
                print('6. Update Company')
                print('7. Delete Employee')
                print('8. Delete Company')
                print('9. Exit')

                choice = input("Enter your choice (1-9): ")
                if choice == '1':
                    create_employee(cursor)
                elif choice == '2':
                    create_company(cursor)
                elif choice == '3':
                    read_employee(cursor)
                elif choice == '4':
                    read_company(cursor)
                elif choice == '5':
                    update_employee(cursor)
                elif choice == '6':
                    update_company(cursor)
                elif choice == '7':
                    delete_employee(cursor)
                elif choice == '8':
                    delete_company(cursor)
                elif choice == '9':
                    break
                else:
                    print("Invalid Choice. Please select a valid option.")
                connection.commit()

if __name__ == '__main__':
    main()
