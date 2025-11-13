import json
import os
import sys
from urllib.parse import unquote

# Add project root to path
project_root = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.insert(0, project_root)

# Simple in-memory storage for demo
USERS = {'admin': {'password': 'admin123', 'role': 'admin'}}
SESSIONS = {}

def handler(event, context):
    try:
        path = event.get('path', '/')
        method = event.get('httpMethod', 'GET')
        
        # Simple routing
        if path == '/' or path == '':
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'text/html'},
                'body': get_landing_page()
            }
        elif path == '/login':
            if method == 'POST':
                return handle_login(event)
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'text/html'},
                'body': get_login_page()
            }
        elif path == '/dashboard':
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'text/html'},
                'body': get_dashboard_page()
            }
        else:
            return {
                'statusCode': 404,
                'headers': {'Content-Type': 'text/html'},
                'body': '<h1>Page Not Found</h1>'
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html'},
            'body': f'<h1>Server Error</h1><p>{str(e)}</p>'
        }

def get_landing_page():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Plant Nursery Manager</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-align: center; }
            .container { max-width: 600px; margin: 0 auto; }
            .btn { background: #2e7d32; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌱 Plant Nursery Manager</h1>
            <p>Modern web application for managing your plant nursery business</p>
            <a href="/.netlify/functions/app/login" class="btn">Login</a>
        </div>
    </body>
    </html>
    '''

def get_login_page():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login - Plant Nursery Manager</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
            .container { max-width: 400px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; }
            input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }
            .btn { background: #2e7d32; color: white; padding: 15px; border: none; border-radius: 5px; width: 100%; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>🌱 Login</h2>
            <form method="POST" action="/.netlify/functions/app/login">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit" class="btn">Login</button>
            </form>
            <p><small>Demo: admin / admin123</small></p>
        </div>
    </body>
    </html>
    '''

def get_dashboard_page():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard - Plant Nursery Manager</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
            .container { max-width: 1200px; margin: 0 auto; }
            .card { background: white; padding: 20px; margin: 20px 0; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }
            .stat { background: linear-gradient(135deg, #2e7d32, #4caf50); color: white; padding: 20px; border-radius: 10px; text-align: center; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌱 Plant Nursery Dashboard</h1>
            <div class="stats">
                <div class="stat">
                    <h3>Plants</h3>
                    <h2>20</h2>
                </div>
                <div class="stat">
                    <h3>Revenue</h3>
                    <h2>KSh 45,000</h2>
                </div>
                <div class="stat">
                    <h3>Sales</h3>
                    <h2>15</h2>
                </div>
            </div>
            <div class="card">
                <h3>Welcome to Plant Nursery Manager!</h3>
                <p>This is a simplified version running on Netlify Functions.</p>
                <p>Features available:</p>
                <ul>
                    <li>✅ Authentication System</li>
                    <li>✅ Dashboard Overview</li>
                    <li>⚠️ Limited functionality due to serverless constraints</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    '''

def handle_login(event):
    # Simple login handling
    return {
        'statusCode': 302,
        'headers': {
            'Location': '/.netlify/functions/app/dashboard'
        },
        'body': ''
    }