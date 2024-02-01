#!/usr/bin/env bash
# Set web servers for deployment

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create folders
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create HTML file
sudo echo "
        <html>
                <head>
                </head>
                <body>
                        Holberton School
                </body>
        </html>
" | sudo tee /data/web_static/releases/test/index.html

# Symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# New Nginx configuration
sudo echo "
server {
    listen 80;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current/;
    }

}

"  | sudo tee /etc/nginx/sites-available/default

# Start Nginx
sudo service nginx start
