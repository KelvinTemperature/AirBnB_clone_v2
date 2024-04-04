#!/usr/bin/env bash
#Sets up web servers for deployment
sudo apt-get -y update
sudo apt-get install nginx -y
sudo service nginx start
sudo ufw allow 'Nginx HTTP'
sudo chown -R "$USER":"$USER" /var/www/html
sudo chmod -R 755 /var/www
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo echo "Hello World!" | sudo tee  /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
exit 0
