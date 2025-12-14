from flask import Blueprint, request, jsonify
from app.services.page_service import PageService

page_bp = Blueprint("pages", __name__)
service = PageService()

# Get a single page by id
@page_bp.get("/<page_id>")
def get_page(page_id):
    return jsonify(service.get_or_create(page_id))

# Filter pages (no page_id)
@page_bp.get("")
def filter_pages():
    return jsonify(service.filter_pages(
        request.args.get("name"),
        request.args.get("industry"),
        int(request.args.get("min_followers", 0)),
        int(request.args.get("max_followers", 10_000_000))
    ))
