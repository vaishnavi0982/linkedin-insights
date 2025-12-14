class Comment:
    def __init__(self, data):
        self.user = data.get("user")
        self.text = data.get("text")
