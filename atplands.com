server {
    listen 80;
    server_name atplands.com www.atplands.com;

    location = /favicon.ico {
        access_log off;
        log_not_found off;
    }

    location /static/ {
        root /home/mbesthc/selmitech;
    }

    location /media/ {
        root /home/mbesthc/selmitech;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/mbesthc/selmitech/realestate.sock;
    }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/atplands.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/atplands.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot   


    # Redirect HTTP to HTTPS
    if ($host = www.atplands.com) {
        return 301 https://$host$request_uri;
    }

    if ($host = atplands.com) {
        return 301 https://$host$request_uri;
    }
}