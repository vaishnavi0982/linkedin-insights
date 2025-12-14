from app.core.database import db

class PostRepository:

    def get_by_page(self, page_id, limit):
        return list(
            db.posts.find({"page_id": page_id}, {"_id": 0}).limit(limit)
        )

    def insert_many(self, posts):
        if posts:
            db.posts.insert_many(posts)
