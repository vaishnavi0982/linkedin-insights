from flask import Flask
from app.core.database import init_db

def create_app():
    app = Flask(__name__)
    init_db()

    from app.api.routes.page_routes import page_bp
    from app.api.routes.post_routes import post_bp
    from app.api.routes.employee_routes import employee_bp
    from app.api.routes.ai_routes import ai_bp

    app.register_blueprint(page_bp, url_prefix="/api/pages")
    app.register_blueprint(post_bp, url_prefix="/api/posts")
    app.register_blueprint(employee_bp, url_prefix="/api/employees")
    app.register_blueprint(ai_bp, url_prefix="/api/ai")

    return app
