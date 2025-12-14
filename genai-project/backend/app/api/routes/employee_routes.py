from flask import Blueprint, jsonify
from app.services.employee_service import EmployeeService

employee_bp = Blueprint("employees", __name__)
service = EmployeeService()

@employee_bp.get("/<page_id>")
def employees(page_id):
    return jsonify(service.get_employees(page_id))
