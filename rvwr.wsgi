#!/usr/bin/env python3

from rvwr import rvwr


rvwr.setup_logging(debug=False, verbose=True)
app = rvwr.config_app('rvwr')
rvwr.BPHandler.register_blueprints(app)
rvwr.config_dabase(app)
application = app

# sudo apt install libapache2-mod-wsgi-py3
"""
"<VirtualHost *>
    #ServerName example.com

    WSGIDaemonProcess rvwr user=rvwr group=rvwr threads=5
    WSGIScriptAlias / /var/www/rvwr/rvwr.wsgi

    <Directory /var/www/rvwr>
        WSGIProcessGroup rvwr
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
"""
