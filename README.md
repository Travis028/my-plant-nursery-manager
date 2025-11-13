# Plant Nursery Manager 🌱

## What It Is
A comprehensive web application designed specifically for managing plant nursery businesses in Kenya. It transforms traditional paper-based nursery operations into a modern, digital management system.

## Core Purpose
- Digitize plant nursery operations from inventory to sales
- Streamline business processes for Kenyan plant nurseries
- Provide real-time insights into business performance
- Enable role-based team management with secure access control

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

## 🌐 Live Demo
**GitHub Pages:** https://travis028.github.io/my-plant-nursery-manager/

**Demo Credentials:**
- Username: `admin`
- Password: `admin123`

## 📁 Repository Structure

### Branches
- **`main`** - Complete application with documentation
- **`frontend`** - HTML templates, CSS, JavaScript, static demo
- **`backend`** - Flask application, models, database, API

### Main Branch Contents
```
my-plant-nursery-manager/
├── lib/                    # Backend Flask application
├── templates/              # Frontend HTML templates  
├── pages/                  # Static demo pages
├── tests/                  # Test suite
├── requirements.txt        # Python dependencies
├── run_web.py             # Application entry point
└── README.md              # This file
```

## Key Features

### 🔐 Authentication & User Management
- Three-tier role system: Admin, Manager, User
- Secure login/logout with session management
- Role-based permissions controlling access
- Admin registration system for team members

### 🌿 Plant Inventory Management
- Complete plant catalog with 20+ Kenyan plants
- Add, edit, delete plants based on permissions
- Real-time inventory tracking with stock counts
- Plant details with names, prices, descriptions

### 💰 Currency & Pricing
- Live USD to KSh conversion using real exchange rates
- Kenyan market focus with KSh pricing display
- Automatic currency updates via external API
- Revenue tracking in local currency

### 📊 Sales & Analytics
- Transaction recording with customer/employee tracking
- Real-time revenue calculations
- Sales history and performance metrics
- Dashboard analytics with trend indicators

## 👥 Role-Based Access Control

**Admin (Red):** Full system access, user management, plant deletion
**Manager (Green):** Plant management, sales recording, data viewing  
**User (Blue):** Inventory viewing, sales recording, analytics access

## 🎨 Technical Features
- **Responsive Design** - Works on all devices
- **Modern UI** - Gradients, animations, FontAwesome icons
- **Role-based Colors** - Visual role identification
- **Live Currency** - Real-time USD to KSh conversion
- **Secure Authentication** - Session-based with role permissions

## 🧪 Testing
```bash
# Run tests
python -m pytest -v

# Test coverage  
python -m pytest --cov=lib tests/
```

## 🤝 Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/name`)
3. Make changes and add tests
4. Commit changes (`git commit -m 'Add feature'`)
5. Push to branch (`git push origin feature/name`)
6. Submit pull request

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

*This project demonstrates modern web development skills while solving real business problems for Kenyan plant nursery operators.*