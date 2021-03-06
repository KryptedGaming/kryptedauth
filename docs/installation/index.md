# Installation

## Docker Installation
We recommend using Docker for production installations. 

### Prerequisites
1. [Install Docker](https://docs.docker.com/get-docker/)
2. [Install Docker Compose](https://docs.docker.com/compose/install/)

### Installation
* Grab our production ready `docker-compose.yml`
```
wget https://raw.githubusercontent.com/KryptedGaming/krypted/development/conf/docker-compose.yml
```
* Grab our recommended `.env` file
```
wget https://raw.githubusercontent.com/KryptedGaming/krypted/development/conf/.env
```
*  Configure `.env`

|   Variable    |    Description   | Example | 
|  -  |  ---  | -- | 
| `DJANGO_SECRET`    |   [Django Secret](https://miniwebtool.com django-secret-key-generator/) used for hashing.  | `aosdfiajsdufihi234h9fasd` (use the generator) | 
| `DEBUG` | Enable Django debugging. | `True` or `False` | 
| `SITE_DOMAIN` | The domain of your site. | `auth.site.com` | 
| `SITE_TITLE` | The title of your site. | `My Site` | 
| `MYSQL_PASSWORD`    |   MYSQL Database password ([generator](https://passwordsgenerator.net/))  | `mypassword` (use the generator) | 
| `INSTALLED_APPS` | Comma separated applications to add to `INSTALLED_APPS` | `django_discord_connector, django_eveonline_connector` | 
| `PIP_INSTALLS` | List of `pip` packages, comma separated. | `django-discord-connector==1.1.0,django-eveonline-timerboard==1.0.2` | 

*  Launch your production environment
```
docker-compose up -d
```

### Advanced Options 

|   Variable    |    Description   | Example | 
|  -  |  ---  | -- | 
| `VERSION`    |   Git branch to checkout. | `master` | 
| `DATABASE` | Your database preference. | `SQLLITE` or `MYSQL` | 
| `MYSQL_DATABASE`    |   MYSQL Database name    | `db` | 
| `MYSQL_USER`    |   MYSQL Database user   | `krypted` | 
| `MYSQL_PORT`    |   MYSQL Database port   | `3306` | 
| `EMAIL_HOST` | Host for your SMTP server. **Enables email verification**. | `myemailserver.com` | 
| `EMAIL_PORT` | Port for your SMTP server. | `123` | 
| `EMAIL_HOST_USER` | User for your SMTP server. | `mail@krypted.com` | 
| `EMAIL_HOST_PASSWORD` | Password for your SMTP server. | `password` | 
| `EMAIL_USE_TLS` | You'll know if you need it. | `True` or `False` | 
| `DEFAULT_FROM_EMAIL` | You'll know if you need it. | None |
| `SITE_PROTOCOL` | Your transfer protocol. | `http://` or `https://`. 
| `GIT_INSTALLS`| List of `pip` packages to install from GitHub, comma separated. <User>/<Repository>| `KryptedGaming/django-eveonline-connector,KryptedGaming/django-discord-connector` |

## Local Installation
We highly recommend **not** doing a local installation for production. This is primarily for developers.

### Prerequisites
* Python3
* Redis
* MySQL (SQLITE3 works, but MYSQL recommended)

### Installation 
* Clone the repository 
```
https://github.com/KryptedGaming/krypted.git
```
* Navigate to directory
```
cd ./krypted
```
* Run the installation script
```
./launcher install
```

### Launching
Use `./launcher` for a list of launch options.


## Serving Containers
Everybody likes to serve containers differently these days, so you'll likely see people doing different things in our Discord. 

### NGINX 
[NGINX](https://www.nginx.com/) is our recommended way of doing things. 

#### Example Configuration 
```
server { 
  listen 80;
  server_name  my.domain;

  location / {
      proxy_pass      http://0.0.0.0:8000;
      proxy_set_header X-Forwarded-Host $server_name;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
  }
}
```

#### Securing NGINX 
Letsencrypt is free and easy. [Ubuntu Example](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04)

### Apache
If you're already on Apache for some reason, feel free to serve in a similar manner. 

#### Example Configuration 
```
<VirtualHost *:80>
    ServerAdmin my@email
    ServerName my.domain

    ProxyPreserveHost On
    ProxyRequests Off
    ProxyPass / http://0.0.0.0:8000/
    ProxyPassReverse / http://0.0.0.0:8000/

</VirtualHost>
```

#### Securing Apache
Same thing, Letsencrypt. If it aint broke, [don't fix it](https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-20-04).

### Traefik 
A lot of people are using Traefik these days, if you're familiar with it you'll just need to make some modifications to the Docker Compose file. 

[More on Traefik](https://doc.traefik.io/traefik/getting-started/quick-start/)


## Paid Installation Service
If you've got ISK and want us to install it for you, [check out this thread.](https://forums.eveonline.com/t/corporation-websites-pathfinder-hosting-and-more/173365?u=bearthatcares)