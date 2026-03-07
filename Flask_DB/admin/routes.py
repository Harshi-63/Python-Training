from flask import Blueprint, render_template


admin = Blueprint('admin', __name__)


@admin.route('/dashboard')
def dashboard():
    return 'admin dashboard'


@admin.route('/settings')
def settngs():
    return 'admin settings'
