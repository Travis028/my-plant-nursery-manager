# Plant Nursery Manager 🌱

A modern web application for managing a plant nursery business, built with Flask and featuring role-based authentication, real-time currency conversion, and a beautiful responsive interface.

## ✨ Features

### 🔐 Authentication & User Management
- **Role-based access control** (Admin, Manager, User)
- **Secure login/logout** system
- **Admin user registration** and management
- **Profile management** with password changes

### 🌿 Plant Inventory Management
- **Add, edit, and delete plants** (role-based permissions)
- **Real-time inventory tracking**
- **20+ pre-seeded Kenyan plants** with realistic pricing
- **Live USD to KSh currency conversion**

### 💰 Sales & Analytics
- **Record sales transactions**
- **Customer and employee tracking**
- **Real-time revenue analytics**
- **Sales history and reporting**

### 🎨 Modern UI/UX
- **Responsive design** with gradient backgrounds
- **FontAwesome icons** and animations
- **Role-based color coding** (Red: Admin, Green: Manager, Blue: User)
- **Real-time statistics** and trend indicators
- **Professional dashboard** with activity overview

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/travis028/my-plant-nursery-manager.git
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

## 🌐 Deployment

### Netlify Deployment

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Deploy to Netlify"
   git push origin main
   ```

2. **Deploy on Netlify:**
   - Go to [netlify.com](https://netlify.com)
   - Connect your GitHub repository
   - Build settings are configured in `netlify.toml`
   - Your app will be live at the generated Netlify URL

## 👥 User Roles & Permissions

### 🔴 Admin
- Register new users and managers
- Delete plants from inventory
- Full system administration
- View all data and analytics
- User management dashboard

### 🟢 Manager
- Add and edit plants in inventory
- Record sales transactions
- View all plants and sales data
- Manage customer information

### 🔵 User
- View plant inventory
- Record sales transactions
- View sales analytics
- Access customer data

## 🏗️ Project Structure

```
my-plant-nursery-manager/
├── lib/                           # Core application
│   ├── web_app.py                # Flask web application
│   ├── database.py               # Database configuration
│   ├── seed_plants.py            # Plant database seeding
│   ├── cli.py                    # Command-line interface
│   └── models/                   # Data models
│       ├── plant.py
│       ├── customer.py
│       ├── employee.py
│       └── sale.py
├── templates/                     # HTML templates
│   ├── base.html                 # Base template with modern styling
│   ├── dashboard.html            # Main dashboard
│   ├── login.html                # Authentication
│   ├── profile.html              # User profile management
│   ├── manage_users.html         # Admin user management
│   └── ...                       # Other feature templates
├── netlify/                       # Netlify deployment
│   └── functions/
│       └── app.py                # Serverless function handler
├── dist/                         # Static files for deployment
├── tests/                        # Test suite
├── netlify.toml                  # Netlify configuration
├── requirements.txt              # Python dependencies
└── README.md
```

## 💱 Currency Features

- **Live exchange rates** from USD to Kenyan Shilling (KSh)
- **Automatic conversion** for pricing display
- **Kenyan market focus** with local plant varieties
- **Real-time rate updates** via external API

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
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 🌟 Screenshots

- **Modern Dashboard:** Real-time stats with animated cards
- **Role-based UI:** Color-coded interface based on user permissions
- **Responsive Design:** Works on desktop, tablet, and mobile
- **Professional Styling:** Gradients, animations, and modern typography

---

**Built with ❤️ for Kenyan plant nursery businesses**


