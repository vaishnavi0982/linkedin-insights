class Page:
    def __init__(self, data):
        self.page_id = data.get("page_id")
        self.name = data.get("name")
        self.url = data.get("url")
        self.description = data.get("description")
        self.industry = data.get("industry")
        self.followers = data.get("followers")
        self.profile_image = data.get("profile_image")
