class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id
        self.projects = []  # List to store assigned projects

    def assign_to_project(self, project):
        if project.add_employee(self):  # Try to add employee to project
            self.projects.append(project)  # Add project to employee's list
        else:
            print(f"Cannot assign {self.name} to project '{project.title}': Project is full.")

    def remove_from_project(self, project):
        if project.remove_employee(self):  # Try to remove employee from project
            self.projects.remove(project)  # Remove project from employee's list

    def view_assigned_projects(self):
        print(f"Projects assigned to {self.name}:")
        for project in self.projects:
            print(f"- {project.title}")


class Project:
    def __init__(self, title, manager, max_employees):
        self.title = title
        self.manager = manager
        self.max_employees = max_employees
        self.employees = []  # List to store assigned employees

    def add_employee(self, employee):
        if len(self.employees) < self.max_employees:
            self.employees.append(employee)
            return True
        else:
            return False

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            return True
        else:
            return False

    def view_assigned_employees(self):
        print(f"Employees assigned to project '{self.title}':")
        for emp in self.employees:
            print(f"- {emp.name} (ID: {emp.id})")


# Sample Usage
# Create employees
employee1 = Employee("John Doe", 101)
employee2 = Employee("Jane Smith", 102)
employee3 = Employee("Alice Johnson", 103)

# Create projects
project1 = Project("Project A", "Manager X", 2)
project2 = Project("Project B", "Manager Y", 3)

# Assign employees to projects
employee1.assign_to_project(project1)
employee2.assign_to_project(project1)  # This will succeed
employee3.assign_to_project(project1)  # This will fail due to project being full

# Assign employee to another project
employee3.assign_to_project(project2)

# View assigned projects for an employee
employee1.view_assigned_projects()
employee3.view_assigned_projects()

# View assigned employees for a project
project1.view_assigned_employees()
project2.view_assigned_employees()

# Remove employee from a project
employee2.remove_from_project(project1)
project1.view_assigned_employees()
