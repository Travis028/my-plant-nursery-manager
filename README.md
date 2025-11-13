# Plant Nursery Manager 🌱

## What It Is
A comprehensive web application designed specifically for managing plant nursery businesses in Kenya. It transforms traditional paper-based nursery operations into a modern, digital management system.

## Core Purpose
- Digitize plant nursery operations from inventory to sales
- Streamline business processes for Kenyan plant nurseries
- Provide real-time insights into business performance
- Enable role-based team management with secure access control

## Key Features

### 🔐 Authentication & User Management
- Three-tier role system: Admin, Manager, User
- Secure login/logout with session management
- Role-based permissions controlling what each user can do
- Admin registration system for adding new team members

### 🌿 Plant Inventory Management
- Complete plant catalog with 20+ pre-loaded Kenyan plants
- Add, edit, delete plants based on user permissions
- Real-time inventory tracking with stock counts
- Plant details including names, prices, and descriptions

### 💰 Currency & Pricing
- Live USD to KSh conversion using real exchange rates
- Kenyan market focus with KSh pricing display
- Automatic currency updates via external API
- Revenue tracking in local currency

### 📊 Sales & Analytics
- Transaction recording with customer and employee tracking
- Real-time revenue calculations
- Sales history and performance metrics
- Dashboard analytics with trend indicators

### 👥 Role-Based Access Control

**Admin (Red):**
- Register new users and managers
- Delete plants from inventory
- Full system administration
- View all data and analytics

**Manager (Green):**
- Add and edit plants in inventory
- Record sales transactions
- View all plants and sales data
- Manage customer information

**User (Blue):**
- View plant inventory
- Record sales transactions
- View sales analytics
- Access customer data

## Technical Architecture

### 🖥️ Backend (Flask Application)
- Python Flask web framework
- SQLAlchemy database management
- SQLite database for data storage
- Session management for user authentication
- API integration for currency conversion

### 🎨 Frontend (Modern Web Interface)
- Responsive HTML templates with mobile support
- CSS gradients and animations for professional look
- FontAwesome icons throughout the interface
- Role-based color coding (Red/Green/Blue themes)
- Interactive dashboard with real-time stats

### 🚀 Deployment Options
- Local development server for testing
- GitHub Pages static demo version
- Netlify serverless deployment option
- Heroku/Railway for full Flask deployment

## Business Value

### 📈 For Nursery Owners
- Digitize operations reducing paperwork
- Track inventory preventing stock-outs
- Monitor revenue with real-time reporting
- Manage team with role-based access

### 👨💼 For Managers
- Streamlined plant management
- Easy sales recording
- Customer relationship tracking
- Performance monitoring

### 👩💻 For Staff
- Simple sales interface
- Quick inventory lookup
- Customer data access
- User-friendly design

## Kenyan Market Focus

### 🇰🇪 Local Adaptation
- KSh currency with live exchange rates
- Kenyan plant varieties in the database
- Local business practices consideration
- Mobile-responsive for smartphone access

### 🌱 Sample Plants Included
- Monstera Deliciosa
- Snake Plant (Sansevieria)
- Fiddle Leaf Fig
- Peace Lily
- Rubber Plant
- Aloe Vera
- Spider Plant
- Pothos
- *...and 12 more varieties*

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Local Development

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

4. **Seed the database:**
   ```bash
   python -m lib.seed_plants
   ```

5. **Run the web application:**
   ```bash
   python run_web.py
   ```

6. **Access the application:**
   Open your browser and go to `http://localhost:5000`

### First Time Setup
- The first user to register becomes the **admin**
- Admin can then register managers and regular users
- No default credentials - secure by design

## 📁 Project Structure

```
my-plant-nursery-manager/
├── lib/                           # Backend code
│   ├── web_app.py                # Flask web application
│   ├── database.py               # Database configuration
│   ├── seed_plants.py            # Plant database seeding
│   ├── cli.py                    # Command-line interface
│   └── models/                   # Data models
│       ├── plant.py
│       ├── customer.py
│       ├── employee.py
│       └── sale.py
├── templates/                     # Frontend templates
│   ├── base.html                 # Base template with modern styling
│   ├── dashboard.html            # Main dashboard
│   ├── login.html                # Authentication
│   ├── profile.html              # User profile management
│   ├── manage_users.html         # Admin user management
│   └── ...                       # Other feature templates
├── pages/                        # Static demo pages
├── dist/                         # Built static files
├── tests/                        # Test suite
├── requirements.txt              # Python dependencies
└── README.md
```

## 🌐 Demo Application

### Live Demo
**GitHub Pages:** https://travis028.github.io/my-plant-nursery-manager/

The deployed version includes:
- Interactive login (admin/admin123)
- Working dashboard with live stats
- Plant inventory showcase
- Navigation between all sections
- Responsive design for all devices

### Demo Credentials
- **Username:** admin
- **Password:** admin123

## 🧪 Testing

```bash
# Run tests
python -m pytest -v

# Test coverage
python -m pytest --cov=lib tests/

# Run CLI version
python -m lib.cli
```

## 🔧 Configuration

- **Database:** SQLite (auto-created)
- **Session Management:** Flask sessions
- **Currency API:** exchangerate-api.com
- **Authentication:** Role-based with secure password storage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🌟 Perfect For
- 🏪 Small to medium plant nurseries
- 🌿 Garden centers
- 🏡 Home-based plant businesses
- 🌳 Agricultural cooperatives
- 📱 Mobile-first operations

---

**Built with ❤️ for Kenyan plant nursery businesses**

*This project demonstrates modern web development skills while solving real business problems for Kenyan plant nursery operators, combining technical excellence with practical business value.*