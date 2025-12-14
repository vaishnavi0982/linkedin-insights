from app.repositories.post_repository import PostRepository
from app.services.scraper_service import LinkedInScraper

class PostService:
    def __init__(self):
        self.repo = PostRepository()
        self.scraper = LinkedInScraper()

    def get_posts(self, page_id: str, limit: int = 10):
        posts = self.repo.get_by_page(page_id, limit)

        if posts:
            return posts

        scraped_posts = self.scraper.scrape_posts(page_id)
        self.repo.insert_many(scraped_posts)

        # Remove _id if present
        for p in scraped_posts:
            p.pop("_id", None)

        return scraped_posts[:limit]
