from app.core.database import db

class EmployeeRepository:

    def get_by_page(self, page_id):
        return list(db.employees.find({"page_id": page_id}, {"_id": 0}))

    def insert_many(self, employees):
        if employees:
            db.employees.insert_many(employees)
