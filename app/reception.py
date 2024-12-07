from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import Patient, Activity
from app.auth import role_required

bp = Blueprint('reception', __name__, url_prefix='/reception')

@bp.route('/dashboard')
@role_required('Reception')
def dashboard():
    recent_patients = Patient.get_all()[:5]  # Get the 5 most recent patients
    return render_template('reception_dashboard.html', recent_patients=recent_patients)

@bp.route('/create_patient', methods=['GET', 'POST'])
@role_required('Reception')
def create_patient():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        age = request.form['age']

        new_patient_id = Patient.create(first_name, last_name, phone_number, age)
        if new_patient_id:
            Activity.create(
                patient_id=new_patient_id,
                patient_name=f"{first_name} {last_name}",
                action="Created new patient",
                admin_name=session.get('username'),
                admin_role=session.get('role')
            )
            flash('Patient created successfully', 'success')
            return redirect(url_for('reception.dashboard'))
        else:
            flash('Error creating patient', 'error')

    return render_template('create_patient.html')

@bp.route('/search')
@role_required('Reception')
def search():
    query = request.args.get('query', '')
    patients = Patient.search(query)
    return render_template('search_results.html', patients=patients, query=query)

@bp.route('/patient/<string:patient_id>')
@role_required('Reception')
def view_patient(patient_id):
    patient = Patient.get_by_id(patient_id)
    if patient:
        return render_template('patient_view.html', patient=patient)
    else:
        flash('Patient not found', 'error')
        return redirect(url_for('reception.dashboard'))

