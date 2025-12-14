class Employee:
    def __init__(self, data):
        self.name = data.get("name")
        self.role = data.get("role")
        self.page_id = data.get("page_id")
