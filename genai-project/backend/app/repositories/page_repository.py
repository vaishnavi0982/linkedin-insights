from app.core.database import db

class PageRepository:

    def find_by_page_id(self, page_id):
        return db.pages.find_one({"page_id": page_id}, {"_id": 0})

    def insert(self, data):
        db.pages.insert_one(data)

    def filter(self, query):
        return list(db.pages.find(query, {"_id": 0}))
