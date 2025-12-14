class Post:
    def __init__(self, data):
        self.post_id = data.get("post_id")
        self.page_id = data.get("page_id")
        self.content = data.get("content")
        self.likes = data.get("likes")
        self.comments = data.get("comments", [])
