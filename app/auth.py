from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from functools import wraps
from app.models import User

bp = Blueprint('auth', __name__)

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'role' not in session:
                flash('Please log in to access this page.', 'error')
                return redirect(url_for('auth.login'))
            if session['role'] not in roles:
                flash('You do not have permission to access this page.', 'error')
                return redirect(url_for('auth.dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        return redirect(url_for('auth.dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.get_by_username(username)
        if user and User.check_password(user, password):
            session['user_id'] = str(user['id'])
            session['username'] = user['username']
            session['role'] = user['role']
            return redirect(url_for('auth.dashboard'))
        flash('Invalid username or password')
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@bp.route('/dashboard')
def dashboard():
    role = session.get('role')
    if role == 'Admin':
        return redirect(url_for('admin.dashboard'))
    elif role == 'Doctor':
        return redirect(url_for('doctor.dashboard'))
    elif role == 'Nurse':
        return redirect(url_for('nurse.dashboard'))
    elif role == 'Reception':
        return redirect(url_for('reception.dashboard'))
    else:
        return redirect(url_for('auth.login'))

