# Netlify Deployment Guide

## Steps to Deploy:

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add Netlify deployment configuration"
   git push origin main
   ```

2. **Connect to Netlify:**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Connect your GitHub repository
   - Select the `my-plant-nursery-manager` repository

3. **Configure Build Settings:**
   - Build command: `pip install -r requirements.txt`
   - Publish directory: `dist`
   - Functions directory: `netlify/functions`

4. **Environment Variables:**
   Add these in Netlify dashboard under Site settings > Environment variables:
   - `PYTHON_VERSION`: `3.8`

5. **Deploy:**
   - Click "Deploy site"
   - Your app will be available at the generated Netlify URL

## Important Notes:
- The database will be reset on each deployment (serverless limitation)
- For production, consider using a cloud database like PostgreSQL
- Sessions may not persist across function calls
- Consider using external authentication service for production

## Alternative: Static Export
For a simpler deployment, consider converting to a static site with a backend API service.