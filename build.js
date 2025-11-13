const fs = require('fs');
const path = require('path');

console.log('🌱 Building Plant Nursery Manager...');

// Create dist directory if it doesn't exist
if (!fs.existsSync('dist')) {
  fs.mkdirSync('dist');
  console.log('📁 Created dist directory');
}

// Create pages directory
if (!fs.existsSync('dist/pages')) {
  fs.mkdirSync('dist/pages');
}

// Copy static files to dist
const indexHtml = `
<!DOCTYPE html>
<html>
<head>
    <title>Plant Nursery Manager</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            margin: 0; 
            padding: 0; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container { 
            max-width: 600px; 
            background: white; 
            padding: 50px; 
            border-radius: 20px; 
            text-align: center; 
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }
        .logo { font-size: 4rem; margin-bottom: 20px; }
        h1 { color: #2e7d32; margin-bottom: 20px; }
        p { color: #666; margin-bottom: 30px; line-height: 1.6; }
        .btn { 
            background: linear-gradient(135deg, #2e7d32, #4caf50); 
            color: white; 
            padding: 15px 30px; 
            text-decoration: none; 
            border-radius: 25px; 
            display: inline-block; 
            margin: 10px; 
            transition: transform 0.3s;
        }
        .btn:hover { transform: translateY(-2px); }
        .features { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); 
            gap: 20px; 
            margin-top: 40px; 
        }
        .feature { 
            padding: 20px; 
            background: #f8f9fa; 
            border-radius: 10px; 
        }
        .feature i { color: #2e7d32; font-size: 2rem; margin-bottom: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🌱</div>
        <h1>Plant Nursery Manager</h1>
        <p>Modern web application for managing your plant nursery business with role-based authentication, real-time currency conversion, and beautiful responsive interface.</p>
        
        <a href="pages/login.html" class="btn">
            <i class="fas fa-sign-in-alt"></i> Launch Application
        </a>
        
        <div class="features">
            <div class="feature">
                <i class="fas fa-users"></i>
                <h4>User Management</h4>
                <p>Role-based access control</p>
            </div>
            <div class="feature">
                <i class="fas fa-seedling"></i>
                <h4>Plant Inventory</h4>
                <p>Complete plant management</p>
            </div>
            <div class="feature">
                <i class="fas fa-chart-line"></i>
                <h4>Sales Analytics</h4>
                <p>Real-time reporting</p>
            </div>
            <div class="feature">
                <i class="fas fa-money-bill-wave"></i>
                <h4>Currency Conversion</h4>
                <p>Live USD to KSh rates</p>
            </div>
        </div>
        
        <div style="margin-top: 40px;">
            <h3>Demo Application</h3>
            <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                <a href="pages/login.html" class="btn">Login Demo</a>
                <a href="pages/dashboard.html" class="btn">Dashboard Demo</a>
                <a href="pages/plants.html" class="btn">Plants Demo</a>
            </div>
        </div>
    </div>
</body>
</html>
`;

// Create demo pages
const loginPage = `
<!DOCTYPE html>
<html>
<head>
    <title>Login - Plant Nursery Manager</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .container { max-width: 400px; background: white; padding: 40px; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
        .logo { text-align: center; font-size: 3rem; margin-bottom: 20px; }
        h2 { color: #2e7d32; text-align: center; margin-bottom: 30px; }
        .form-group { margin-bottom: 20px; }
        label { display: block; margin-bottom: 5px; color: #333; font-weight: 600; }
        input { width: 100%; padding: 12px; border: 2px solid #e0e0e0; border-radius: 8px; font-size: 16px; }
        input:focus { border-color: #2e7d32; outline: none; }
        .btn { background: linear-gradient(135deg, #2e7d32, #4caf50); color: white; padding: 12px 24px; border: none; border-radius: 8px; width: 100%; font-size: 16px; cursor: pointer; }
        .btn:hover { transform: translateY(-2px); }
        .demo-info { background: #e8f5e8; padding: 15px; border-radius: 8px; margin-top: 20px; text-align: center; }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🌱</div>
        <h2>Login to Plant Nursery</h2>
        <form onsubmit="handleLogin(event)">
            <div class="form-group">
                <label>Username</label>
                <input type="text" id="username" value="admin" required>
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" id="password" value="admin123" required>
            </div>
            <button type="submit" class="btn">Login</button>
        </form>
        <div class="demo-info">
            <strong>Demo Credentials:</strong><br>
            Username: admin<br>
            Password: admin123
        </div>
    </div>
    <script>
        function handleLogin(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            if (username === 'admin' && password === 'admin123') {
                localStorage.setItem('user', username);
                localStorage.setItem('role', 'admin');
                window.location.href = 'dashboard.html';
            } else {
                alert('Invalid credentials! Use admin/admin123');
            }
        }
    </script>
</body>
</html>
`;

const dashboardPage = `
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard - Plant Nursery Manager</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 0; background: #f5f5f5; }
        .header { background: linear-gradient(135deg, #2e7d32, #4caf50); color: white; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .nav { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 40px; }
        .stat-card { background: white; padding: 25px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); text-align: center; }
        .stat-number { font-size: 2.5rem; font-weight: 700; margin-bottom: 10px; }
        .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
        .card { background: white; padding: 30px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); text-align: center; }
        .btn { background: linear-gradient(135deg, #2e7d32, #4caf50); color: white; padding: 12px 24px; border: none; border-radius: 8px; text-decoration: none; display: inline-block; margin: 5px; }
        .btn:hover { transform: translateY(-2px); }
    </style>
</head>
<body>
    <div class="header">
        <div class="container">
            <div class="nav">
                <h1>🌱 Plant Nursery Manager</h1>
                <div>
                    <span id="welcome">Welcome, Admin!</span>
                    <a href="../index.html" class="btn">Logout</a>
                </div>
            </div>
        </div>
    </div>
    
    <div class="container">
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number" style="color: #2e7d32;">25</div>
                <div>Plants in Stock</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" style="color: #f57c00;">KSh 45,000</div>
                <div>Total Revenue</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" style="color: #1976d2;">12</div>
                <div>Sales Today</div>
            </div>
        </div>
        
        <div class="cards">
            <div class="card">
                <i class="fas fa-seedling" style="font-size: 3rem; color: #2e7d32; margin-bottom: 20px;"></i>
                <h3>Plant Inventory</h3>
                <p>Manage your complete plant collection with detailed information and pricing.</p>
                <a href="plants.html" class="btn">View Plants</a>
            </div>
            <div class="card">
                <i class="fas fa-chart-line" style="font-size: 3rem; color: #f57c00; margin-bottom: 20px;"></i>
                <h3>Sales Analytics</h3>
                <p>Track your sales performance and revenue with detailed analytics.</p>
                <a href="#" class="btn">View Sales</a>
            </div>
            <div class="card">
                <i class="fas fa-users" style="font-size: 3rem; color: #1976d2; margin-bottom: 20px;"></i>
                <h3>User Management</h3>
                <p>Manage user accounts and permissions for your nursery staff.</p>
                <a href="#" class="btn">Manage Users</a>
            </div>
        </div>
    </div>
</body>
</html>
`;

const plantsPage = `
<!DOCTYPE html>
<html>
<head>
    <title>Plants - Plant Nursery Manager</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { font-family: 'Segoe UI', sans-serif; margin: 0; background: #f5f5f5; }
        .header { background: linear-gradient(135deg, #2e7d32, #4caf50); color: white; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .nav { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
        .plants-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
        .plant-card { background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
        .plant-image { height: 200px; background: linear-gradient(135deg, #e8f5e8, #c8e6c9); display: flex; align-items: center; justify-content: center; font-size: 4rem; }
        .plant-info { padding: 20px; }
        .plant-name { font-size: 1.2rem; font-weight: 600; margin-bottom: 10px; color: #2e7d32; }
        .plant-price { font-size: 1.5rem; font-weight: 700; color: #f57c00; margin-bottom: 15px; }
        .btn { background: linear-gradient(135deg, #2e7d32, #4caf50); color: white; padding: 8px 16px; border: none; border-radius: 6px; text-decoration: none; display: inline-block; }
    </style>
</head>
<body>
    <div class="header">
        <div class="container">
            <div class="nav">
                <h1>🌱 Plant Inventory</h1>
                <a href="dashboard.html" class="btn">Back to Dashboard</a>
            </div>
        </div>
    </div>
    
    <div class="container">
        <div class="plants-grid" id="plantsGrid"></div>
    </div>
    
    <script>
        const plants = [
            { name: 'Monstera Deliciosa', price: 'KSh 2,500', icon: '🌿' },
            { name: 'Snake Plant', price: 'KSh 1,200', icon: '🐍' },
            { name: 'Fiddle Leaf Fig', price: 'KSh 3,500', icon: '🌱' },
            { name: 'Peace Lily', price: 'KSh 1,800', icon: '🕊️' },
            { name: 'Rubber Plant', price: 'KSh 2,200', icon: '🌳' },
            { name: 'Aloe Vera', price: 'KSh 800', icon: '🌵' },
            { name: 'Spider Plant', price: 'KSh 1,000', icon: '🕷️' },
            { name: 'Pothos', price: 'KSh 1,500', icon: '🍃' }
        ];
        
        const grid = document.getElementById('plantsGrid');
        plants.forEach(plant => {
            const card = document.createElement('div');
            card.className = 'plant-card';
            card.innerHTML = \`
                <div class="plant-image">\${plant.icon}</div>
                <div class="plant-info">
                    <div class="plant-name">\${plant.name}</div>
                    <div class="plant-price">\${plant.price}</div>
                    <a href="#" class="btn">View Details</a>
                </div>
            \`;
            grid.appendChild(card);
        });
    </script>
</body>
</html>
`;

try {
  fs.writeFileSync('dist/index.html', indexHtml);
  fs.writeFileSync('dist/pages/login.html', loginPage);
  fs.writeFileSync('dist/pages/dashboard.html', dashboardPage);
  fs.writeFileSync('dist/pages/plants.html', plantsPage);
  
  // Copy to root as well
  fs.writeFileSync('index.html', indexHtml);
  
  console.log('✅ Created index.html');
  console.log('✅ Created login demo page');
  console.log('✅ Created dashboard demo page');
  console.log('✅ Created plants demo page');
  console.log('✅ Build completed successfully!');
  console.log('🚀 Ready for deployment');
} catch (error) {
  console.error('❌ Build failed:', error);
  process.exit(1);
}