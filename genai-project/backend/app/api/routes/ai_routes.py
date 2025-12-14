from flask import Blueprint, jsonify
from app.services.ai_service import AIService
from app.services.page_service import PageService
from app.services.post_service import PostService

ai_bp = Blueprint("ai", __name__)
ai_service = AIService()
page_service = PageService()
post_service = PostService()

@ai_bp.get("/summary/<page_id>")
def generate_summary(page_id):
    page_data = page_service.get_or_create(page_id)
    posts = post_service.get_posts(page_id, limit=5)

    summary = ai_service.generate_summary(page_data, posts)
    return jsonify({"page_id": page_id, "summary": summary})
