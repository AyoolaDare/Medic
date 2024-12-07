from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import Patient, Activity
from app.auth import role_required

bp = Blueprint('nurse', __name__, url_prefix='/nurse')

@bp.route('/dashboard')
@role_required('Nurse')
def dashboard():
    patients = Patient.get_all()
    recent_activities = Activity.get_recent(limit=10)
    
    return render_template('nurse_dashboard.html', patients=patients, recent_activities=recent_activities)

@bp.route('/search')
@role_required('Nurse')
def search():
    query = request.args.get('query', '')
    patients = Patient.search(query)
    return render_template('search_results.html', patients=patients, query=query)

@bp.route('/patient/<string:patient_id>')
@role_required('Nurse')
def view_patient(patient_id):
    patient = Patient.get_by_id(patient_id)
    if patient:
        return render_template('patient_view.html', patient=patient)
    else:
        flash('Patient not found', 'error')
        return redirect(url_for('nurse.dashboard'))

@bp.route('/patient/<string:patient_id>/update', methods=['GET', 'POST'])
@role_required('Nurse')
def update_patient(patient_id):
    patient = Patient.get_by_id(patient_id)
    if not patient:
        flash('Patient not found', 'error')
        return redirect(url_for('nurse.dashboard'))

    if request.method == 'POST':
        # Update patient information
        data = {
            'weight': request.form['weight'],
            'height': request.form['height'],
            'blood_pressure': request.form['blood_pressure']
        }
        if Patient.update(patient_id, data):
            Activity.create(
                patient_id=patient_id,
                patient_name=f"{patient['first_name']} {patient['last_name']}",
                action="Updated patient information",
                admin_name=session.get('username'),
                admin_role=session.get('role')
            )
            flash('Patient information updated successfully', 'success')
            return redirect(url_for('nurse.view_patient', patient_id=patient_id))
        else:
            flash('Error updating patient information', 'error')

    return render_template('patient_update.html', patient=patient)

