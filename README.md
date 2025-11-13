# Plant Nursery Manager

A command-line and web application for managing a plant nursery, built with Python and SQLAlchemy.

## Features

- Manage plant inventory
- Track customers and employees
- Record sales transactions
- Web interface with role-based authentication
- Real-time currency conversion (USD to KSh)
- Comprehensive test coverage

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- SQLite (included with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/travis028/my-plant-nursery-manager.git
   cd my-plant-nursery-manager
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Web Application

```bash
python run_web.py
```

Then open your browser and go to `http://localhost:5000`

### Running the CLI Application

```bash
python -m lib.cli
```

### Available Commands

- **Add a new plant** to inventory
- **List all plants** in inventory
- **Record a sale** with customer and employee details
- **View sales history**

### Database Setup

The application uses SQLite by default. To seed the database with sample plants:

```bash
python -m lib.seed_plants
```

## Testing

To run the test suite:

```bash
python -m pytest -v
```

For test coverage report:

```bash
python -m pytest --cov=lib tests/
```

## Project Structure

```
my-plant-nursery-manager/
├── lib/                    # Main package
│   ├── __init__.py        # Package initialization
│   ├── cli.py             # Command-line interface
│   ├── web_app.py         # Web application
│   ├── database.py        # Database configuration
│   ├── seed_plants.py     # Database seeding
│   └── models/            # Data models
│       ├── __init__.py
│       ├── plant.py
│       ├── customer.py
│       ├── employee.py
│       └── sale.py
├── templates/             # HTML templates
├── tests/                
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_models.py
│   └── test_seed.py
├── requirements.txt    
├── run_web.py             # Web app entry point
└── README.md            
```

## License

MIT License