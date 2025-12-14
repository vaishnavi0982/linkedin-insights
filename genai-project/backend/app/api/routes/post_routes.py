from flask import Blueprint, jsonify, request
from app.services.post_service import PostService

post_bp = Blueprint("posts", __name__)
service = PostService()

@post_bp.get("/<page_id>")
def get_posts(page_id):
    limit = int(request.args.get("limit", 10))
    return jsonify(service.get_posts(page_id, limit))
