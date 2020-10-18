# rvwr-backend

A basic API for receiving & storing reviews. Supports sms reviews via Twilio

A front-end (UI) for this project is located [here](https://github.com/dpat/rvwrfront).

RVWR Testing site is currently running at open-sms.com/

## Prereqs

Requirements are meant to be installed via pip, the requirements likely exist
from apt, but the project was designed to run with pip.
```
$ pip3 install -r requirements.txt
```

## Install

This api is meant to be run as a command line script, after installation.  The
prereqs will be installed while the package is being installed and ready to go.
```
$ pip3 install .
```

### Database
rvwr needs to setup a database to store the reviews, products, users, etc.
First the database needs to be created.  Currently rvwr runs on an sqlite
database and is stored /opt/rvwr/rvwr.db.
```
$ rvwr init
```

### Token
Any request that requires a write operation (delete, post, put) requires a
token generated from rvwr and stored in the database.  This is to help
prevent unwanted users from deleting and modifying existing data.  To generate
a new token run
```
$ rvwr token
```
To view existing tokens run
```
$ rvwr token --list
```
Tokens must be sent as a header with write required requests under the name
token.  i.e. Token=<string of characters> inside the headers of the request.
Headers were chosen to pass the token instead of URL parameters for security
reasons.  I understand that this can be tricky with javascript.


### Installing and running rvwr (for use w/ digital ocean Ubuntu)

apt-get update   
apt-get install -y pinentry-curses xz-utils python3-pip git   
apt-get clean   

cd ~   
pip3 install virtualenv   
virtualenv venv   
ENV PATH="~/venv/bin/activate:${PATH}"   

apt-get update   
apt-get install -y apache2 libapache2-mod-wsgi-py3 python3-dev   
apt-get clean   

cd ~   
git clone https://github.com/dpat/rvwrfront.git   
git clone https://github.com/dpat/rvwr-backend.git   
cd rvwr-backend   
pip3 install -r requirements.txt   
pip3 install .   
rvwr init   

cp rvwrfront_wsgi.txt ~/rvwrfront_wsgi.txt   
cp rvwr_backend_wsgi.txt ~/rvwr_backend_wsgi.txt   
cp rvwr_conf.txt ~/rvwr_conf.txt   

cd ~/rvwr_backend   
TOKEN="$(rvwr token)"   

cd ~   
sed -i "s@placeholder_num@$NUMBER@g" rvwr-backend_wsgi.txt   
sed -i "s@placeholder_url@$DOMAIN@g" rvwr-backend_wsgi.txt   
sed -i "s@placeholder_auth_token@$AUTH_TOKEN@g" rvwr-backend_wsgi.txt   

sed -i "s@placeholder_url@$DOMAIN@g" rvwrfront_wsgi.txt   
sed -i "s@placeholder_token@$TOKEN@g" rvwrfront_wsgi.txt   
sed -i "s@placeholder_pass@$PASSWORD@g" rvwrfront_wsgi.txt   


sed -i "s@placeholder_url@$DOMAIN@g" rvwr_conf.txt   

echo "$IP $DOMAIN" >> /etc/hosts   
echo "$IP sms.$DOMAIN" >> /etc/hosts   

mkdir /var/www/rvwr-backend   
mkdir /var/www/rvwrfront   
cp -r rvwrfront /var/www/rvwrfront/.   
cp rvwr-backend_wsgi.txt /var/www/rvwr-backend/rvwr-backend.wsgi   
cp rvwrfront_wsgi.txt /var/www/rvwrfront/rvwrfront.wsgi   
cp rvwr_conf.txt /etc/apache2/sites-available/rvwr.conf   
cp rvwr_conf.txt /etc/apache2/sites-enabled/rvwr.con   

chmod 777 /opt/rvwr/rvwr.db   
chmod 777 /opt/rvwr/   

service apache2 restart


###TODO:
- Add single user URLS
- HTTPS upgrade from http
- Authentication for admins
- Separate out viewing and posting reviews
- Change routes to support companies
- Change database fields to support companies
- Add routes to support user numbers
- Add Database routes to support user numbers
- Setup Twilio initiation messaging
