# 🌱 Plant Nursery Manager

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://my-plant-nursery-manager.onrender.com)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/Travis028/my-plant-nursery-manager/actions)

A comprehensive plant nursery management system built with Python, SQLAlchemy, and Flask. Features both command-line and web interfaces for managing plant inventory, sales, customers, employees, and user administration.

## ✨ Features

### 🌿 Plant Management
- **Add/Edit Plants**: Create and modify plant inventory with pricing
- **Plant Inventory**: View all plants with real-time stock information
- **Price Management**: Automatic USD to KSh currency conversion
- **Plant Search**: Find plants by name or ID

### 👥 User Management & Authentication
- **Role-Based Access Control**: Admin, Manager, and User roles
- **Active User Tracking**: Real-time monitoring of logged-in users
- **User Registration**: Admin-controlled user creation
- **Session Management**: Secure login/logout with session tracking
- **Profile Management**: User profile editing and password updates

### 💰 Sales & Transactions
- **Record Sales**: Process transactions with customer and employee tracking
- **Sales History**: Comprehensive sales analytics and reporting
- **Revenue Tracking**: Real-time revenue calculations in KSh
- **Customer Management**: Automatic customer record creation
- **Employee Tracking**: Sales attribution to employees

### 🖥️ Interfaces
- **Web Interface**: Modern, responsive web application
- **CLI Interface**: Command-line tools for quick operations
- **RESTful API**: Programmatic access to all features
- **Real-time Updates**: Live dashboard with current statistics

### 🛠️ Technical Features
- **Database**: SQLite with SQLAlchemy ORM
- **Migrations**: Alembic database migration support
- **Testing**: Comprehensive test suite with pytest
- **Deployment**: Ready for Render, Heroku, and other platforms
- **CI/CD**: GitHub Actions workflow for automated deployment

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Travis028/my-plant-nursery-manager.git
   cd my-plant-nursery-manager
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Seed the database (optional):**
   ```bash
   python -m lib.seed_plants
   ```

## 📖 Usage

### Web Application

Start the web server:
```bash
python run_web.py
```

Access the application at `http://localhost:5000`

#### User Roles & Permissions

- **👑 Admin**:
  - Full system access
  - User management (create/delete users)
  - Plant management (add/edit/delete)
  - View all data and analytics
  - Access to active user monitoring

- **👔 Manager**:
  - Add and edit plants
  - Record sales transactions
  - View all plant and sales data
  - Access to dashboard analytics

- **👤 User**:
  - View plant inventory
  - Record sales transactions
  - View personal sales history

### Command Line Interface

Run CLI commands:
```bash
python -m lib.cli
```

Available commands:
- `list_plants` - Display all plants in inventory
- `add_plant` - Add a new plant to inventory
- `record_sale` - Record a new sale transaction
- `list_sales` - View sales history

### API Endpoints

The web application provides RESTful API endpoints:

- `GET /` - Landing page
- `POST /login` - User authentication
- `GET /dashboard` - Main dashboard
- `GET /plants` - Plant inventory
- `POST /add_plant` - Add new plant (Manager+)
- `POST /edit_plant/<id>` - Edit plant (Manager+)
- `POST /delete_plant/<id>` - Delete plant (Admin only)
- `GET /sales` - Sales history
- `POST /record_sale` - Record sale
- `GET/POST /manage_users` - User management (Admin only)
- `GET/POST /profile` - User profile

## 🏗️ Project Structure

```
my-plant-nursery-manager/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions CI/CD
├── lib/                        # Main application package
│   ├── __init__.py            # Package initialization
│   ├── cli.py                 # Command-line interface
│   ├── web_app.py             # Flask web application
│   ├── database.py            # Database configuration
│   ├── seed_plants.py         # Database seeding script
│   ├── debug.py               # Debugging utilities
│   ├── helpers.py             # Helper functions
│   └── models/                # SQLAlchemy models
│       ├── __init__.py
│       ├── plant.py           # Plant model
│       ├── customer.py        # Customer model
│       ├── employee.py        # Employee model
│       └── sale.py            # Sale model
├── templates/                 # Jinja2 HTML templates
│   ├── base.html              # Base template
│   ├── dashboard.html         # Main dashboard
│   ├── login.html             # Login page
│   ├── register.html          # Admin registration
│   ├── plants.html            # Plant inventory
│   ├── add_plant.html         # Add plant form
│   ├── edit_plant.html        # Edit plant form
│   ├── sales.html             # Sales history
│   ├── record_sale.html       # Record sale form
│   ├── manage_users.html      # User management (Admin)
│   ├── profile.html           # User profile
│   └── landing.html           # Landing page
├── tests/                     # Test suite
│   ├── __init__.py
│   ├── test_cli.py            # CLI tests
│   ├── test_models.py         # Model tests
│   └── test_seed.py           # Seeding tests
├── .env                       # Environment variables
├── Pipfile                    # Pipenv dependencies
├── Pipfile.lock               # Locked dependencies
├── Procfile                   # Heroku deployment
├── render.yaml                # Render deployment
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup
├── run_web.py                 # Web app entry point
├── alembic.ini               # Database migrations
├── nursery.db                # SQLite database
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## 🧪 Testing

Run the complete test suite:
```bash
python -m pytest -v
```

Run tests with coverage report:
```bash
python -m pytest --cov=lib tests/
```

Run specific test files:
```bash
python -m pytest tests/test_models.py
python -m pytest tests/test_cli.py
```

## 🚀 Deployment

### Render (Recommended)
1. Connect your GitHub repository to Render
2. Use the `render.yaml` configuration
3. Deploy automatically on push to main branch

### Heroku
1. Create a new Heroku app
2. Set buildpack to Python
3. Use `Procfile` for process definition
4. Deploy via git push

### Manual Deployment
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_ENV=production
export SECRET_KEY=your-secret-key-here

# Run with gunicorn
gunicorn run_web:app
```

## 🔧 Configuration

### Environment Variables
- `FLASK_ENV`: Set to `production` for live deployment
- `SECRET_KEY`: Flask secret key for sessions
- `DATABASE_URL`: Database connection string (defaults to SQLite)

### Database
The application uses SQLite by default. For production, configure PostgreSQL:

```python
# In database.py
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///nursery.db')
```

## 📊 Database Schema

### Plants Table
- `id`: Primary key
- `name`: Plant name (required, min 2 chars)
- `price`: Price in USD (stored as cents)

### Customers Table
- `id`: Primary key
- `name`: Customer name

### Employees Table
- `id`: Primary key
- `name`: Employee name

### Sales Table
- `id`: Primary key
- `plant_id`: Foreign key to plants
- `customer_id`: Foreign key to customers
- `employee_id`: Foreign key to employees
- `timestamp`: Sale timestamp

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests before committing
python -m pytest

# Format code
black lib/ tests/
```

## 📝 API Documentation

### Authentication
All protected endpoints require user authentication via Flask sessions.

### Response Format
All API responses return JSON with consistent structure:
```json
{
  "success": true,
  "data": {...},
  "message": "Operation successful"
}
```

## 🐛 Troubleshooting

### Common Issues

1. **Database connection errors**:
   - Ensure SQLite file permissions
   - Check DATABASE_URL environment variable

2. **Import errors**:
   - Activate virtual environment
   - Install all requirements: `pip install -r requirements.txt`

3. **Permission errors**:
   - Check user roles in admin panel
   - Ensure proper authentication

### Debug Mode
Enable debug logging:
```bash
export FLASK_DEBUG=1
python run_web.py
```

## 📈 Performance

- **Database Optimization**: Uses SQLAlchemy connection pooling
- **Caching**: Flask session caching for user data
- **Lazy Loading**: Optimized database queries with joinedload
- **Currency Conversion**: Cached exchange rates with fallback

## 🔒 Security

- **Session Management**: Secure Flask sessions with secret keys
- **Input Validation**: SQLAlchemy model validators
- **Role-Based Access**: Granular permission system
- **CSRF Protection**: Flask-WTF integration
- **Password Security**: Secure password storage (upgrade recommended)

## 📚 Dependencies

### Core Dependencies
- **Flask**: Web framework
- **SQLAlchemy**: Database ORM
- **Werkzeug**: WSGI utility
- **Requests**: HTTP client for currency API
- **Click**: CLI framework

### Development Dependencies
- **pytest**: Testing framework
- **pytest-cov**: Coverage reporting
- **black**: Code formatting
- **flake8**: Linting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Flask and SQLAlchemy
- Currency conversion via ExchangeRate-API
- Icons from Font Awesome
- UI inspired by modern web design principles

## 📞 Support

For support, please open an issue on GitHub or contact the maintainers.

---

**Made with ❤️ for plant nursery management**
# Additional development notes
