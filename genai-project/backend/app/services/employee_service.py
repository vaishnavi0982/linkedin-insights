from app.repositories.employee_repository import EmployeeRepository
from app.services.scraper_service import LinkedInScraper

class EmployeeService:

    def __init__(self):
        self.repo = EmployeeRepository()
        self.scraper = LinkedInScraper()

    def get_employees(self, page_id):
        employees = self.repo.get_by_page(page_id)
        if employees:
            return employees

        scraped = self.scraper.scrape_employees(page_id)
        self.repo.insert_many(scraped)
        return scraped
