# Backend - Plant Nursery Manager ⚙️

## Overview
This branch contains the backend Flask application for the Plant Nursery Manager, including database models, API endpoints, authentication, and business logic.

## 📁 Structure
```
backend/
├── lib/                      # Core application code
│   ├── web_app.py           # Flask application & routes
│   ├── database.py          # Database configuration
│   ├── seed_plants.py       # Database seeding
│   ├── cli.py              # Command-line interface
│   └── models/             # Data models
│       ├── plant.py        # Plant model
│       ├── customer.py     # Customer model
│       ├── employee.py     # Employee model
│       └── sale.py         # Sale model
├── tests/                  # Test suite
├── requirements.txt        # Python dependencies
├── run_web.py             # Application entry point
└── nursery.db            # SQLite database
```

## 🔧 Technologies
- **Flask** - Web framework
- **SQLAlchemy** - Database ORM
- **SQLite** - Database
- **Requests** - HTTP client for currency API
- **Pytest** - Testing framework

## 🚀 Setup & Installation
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Seed database
python -m lib.seed_plants

# Run application
python run_web.py
```

## 🔐 Authentication
- Session-based authentication
- Role-based access control (Admin, Manager, User)
- Secure password handling
- Protected routes with decorators

## 💰 Currency Integration
- Live USD to KSh conversion
- External API integration (exchangerate-api.com)
- Automatic rate updates
- Local currency display

## 📊 Database Models
- **Plant**: name, price (USD), timestamps
- **Customer**: name, contact info
- **Employee**: name, role
- **Sale**: plant, customer, employee, timestamp

## 🧪 Testing
```bash
# Run tests
python -m pytest -v

# Test coverage
python -m pytest --cov=lib tests/
```

## 🔌 API Endpoints
- `/` - Landing page
- `/login` - Authentication
- `/dashboard` - Main dashboard
- `/plants` - Plant inventory
- `/add_plant` - Add new plant (Manager+)
- `/sales` - Sales management
- `/profile` - User profile
- `/manage_users` - User management (Admin)