from app.repositories.page_repository import PageRepository
from app.services.scraper_service import LinkedInScraper

class PageService:

    def __init__(self):
        self.repo = PageRepository()
        self.scraper = LinkedInScraper()

    def get_or_create(self, page_id):
        page = self.repo.find_by_page_id(page_id)
        if page:
            return page

        data = self.scraper.scrape_page(page_id)
        self.repo.insert(data)
        return data

    def filter_pages(self, name, industry, min_followers, max_followers):
        query = {
            "followers": {"$gte": min_followers, "$lte": max_followers}
        }
        if name:
            query["name"] = {"$regex": name, "$options": "i"}
        if industry:
            query["industry"] = industry

        return self.repo.filter(query)
