from flask import Flask, render_template, request, redirect, url_for, flash, session as flask_session
from sqlalchemy.orm import joinedload
from .database import Session
from . import Plant, Customer, Employee, Sale
import os
import requests
from functools import wraps

# Get the parent directory of lib to find templates
template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'your-secret-key-here'

# Simple user credentials (in production, use proper database)
USERS = {}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in flask_session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in flask_session or USERS.get(flask_session['user'], {}).get('role') != 'admin':
            flash('Admin access required', 'error')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

def manager_or_admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in flask_session:
            return redirect(url_for('login'))
        user_role = USERS.get(flask_session['user'], {}).get('role')
        if user_role not in ['admin', 'manager']:
            flash('Manager or Admin access required', 'error')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated_function

# Get USD to KSh exchange rate
def get_usd_to_ksh_rate():
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD', timeout=5)
        data = response.json()
        return data['rates']['KES']
    except:
        return 130.0

def format_ksh(amount_usd):
    ksh_rate = get_usd_to_ksh_rate()
    ksh_amount = amount_usd * ksh_rate
    return f"KSh {ksh_amount:,.2f}"

app.jinja_env.filters['ksh'] = format_ksh

@app.context_processor
def inject_ksh_rate():
    return dict(ksh_rate=get_usd_to_ksh_rate, users=USERS)

@app.route('/')
def landing():
    if 'user' in flask_session:
        return redirect(url_for('dashboard'))
    return render_template('landing.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if this is the first user (admin setup)
    if len(USERS) > 0:
        flash('Registration is closed. Contact admin for access.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username and password:
            USERS[username] = {'password': password, 'role': 'admin'}
            flask_session['user'] = username
            flash('Admin account created successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Username and password required', 'error')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # If no users exist, redirect to registration
    if len(USERS) == 0:
        return redirect(url_for('register'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in USERS and USERS[username]['password'] == password:
            flask_session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    flask_session.pop('user', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('landing'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    username = flask_session['user']
    user_data = USERS.get(username, {})
    
    if request.method == 'POST':
        new_password = request.form.get('password')
        if new_password:
            USERS[username]['password'] = new_password
            flash('Password updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    # Get plants count for admin overview
    session = Session()
    plants_count = session.query(Plant).count()
    session.close()
    
    return render_template('profile.html', user_data=user_data, username=username, 
                         users=USERS, plants_count=plants_count)

@app.route('/manage_users', methods=['GET', 'POST'])
@admin_required
def manage_users():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        
        if username and password and role:
            USERS[username] = {'password': password, 'role': role}
            flash(f'{role.title()} {username} added successfully!', 'success')
        else:
            flash('All fields required', 'error')
    
    return render_template('manage_users.html', users=USERS)

@app.route('/dashboard')
@login_required
def dashboard():
    session = Session()
    plants_count = session.query(Plant).count()
    sales_count = session.query(Sale).count()
    total_revenue_usd = sum([sale.plant.price for sale in session.query(Sale).options(joinedload(Sale.plant)).all()])
    ksh_rate = get_usd_to_ksh_rate()
    total_revenue_ksh = total_revenue_usd * ksh_rate
    session.close()
    
    return render_template('dashboard.html', 
                         plants_count=plants_count,
                         sales_count=sales_count,
                         total_revenue=f"{total_revenue_ksh:,.2f}",
                         users=USERS)

@app.route('/plants')
@login_required
def plants():
    session = Session()
    plants = session.query(Plant).all()
    session.close()
    return render_template('plants.html', plants=plants)

@app.route('/add_plant', methods=['GET', 'POST'])
@manager_or_admin_required
def add_plant():
    if request.method == 'POST':
        session = Session()
        try:
            name = request.form['name']
            price_ksh = float(request.form['price'])
            ksh_rate = get_usd_to_ksh_rate()
            price_usd = price_ksh / ksh_rate
            plant = Plant(name=name, price=price_usd)
            session.add(plant)
            session.commit()
            flash('Plant added successfully!', 'success')
        except ValueError as e:
            flash(f'Error: {str(e)}', 'error')
        finally:
            session.close()
        return redirect(url_for('plants'))
    return render_template('add_plant.html')

@app.route('/edit_plant/<int:plant_id>', methods=['GET', 'POST'])
@manager_or_admin_required
def edit_plant(plant_id):
    session = Session()
    plant = session.query(Plant).get(plant_id)
    if not plant:
        flash('Plant not found', 'error')
        return redirect(url_for('plants'))
    
    if request.method == 'POST':
        try:
            plant.name = request.form['name']
            price_ksh = float(request.form['price'])
            ksh_rate = get_usd_to_ksh_rate()
            plant.price = price_ksh / ksh_rate
            session.commit()
            flash('Plant updated successfully!', 'success')
        except ValueError as e:
            flash(f'Error: {str(e)}', 'error')
        finally:
            session.close()
        return redirect(url_for('plants'))
    
    session.close()
    return render_template('edit_plant.html', plant=plant)

@app.route('/delete_plant/<int:plant_id>')
@admin_required
def delete_plant(plant_id):
    session = Session()
    plant = session.query(Plant).get(plant_id)
    if plant:
        session.delete(plant)
        session.commit()
        flash('Plant deleted successfully!', 'success')
    else:
        flash('Plant not found', 'error')
    session.close()
    return redirect(url_for('plants'))

@app.route('/sales')
@login_required
def sales():
    session = Session()
    sales = session.query(Sale).options(
        joinedload(Sale.plant),
        joinedload(Sale.customer),
        joinedload(Sale.employee)
    ).all()
    session.close()
    return render_template('sales.html', sales=sales)

@app.route('/record_sale', methods=['GET', 'POST'])
@login_required
def record_sale():
    session = Session()
    if request.method == 'POST':
        try:
            plant_id = int(request.form['plant_id'])
            customer_name = request.form['customer_name']
            employee_name = request.form['employee_name']

            customer = session.query(Customer).filter_by(name=customer_name).first()
            if not customer:
                customer = Customer(name=customer_name)
                session.add(customer)

            employee = session.query(Employee).filter_by(name=employee_name).first()
            if not employee:
                employee = Employee(name=employee_name)
                session.add(employee)

            plant = session.query(Plant).get(plant_id)
            if not plant:
                flash('Invalid plant selected', 'error')
                return redirect(url_for('record_sale'))

            sale = Sale(plant=plant, customer=customer, employee=employee)
            session.add(sale)
            session.commit()
            flash('Sale recorded successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
        finally:
            session.close()
        return redirect(url_for('sales'))
    
    plants = session.query(Plant).all()
    session.close()
    return render_template('record_sale.html', plants=plants)

if __name__ == '__main__':
    app.run(debug=True)