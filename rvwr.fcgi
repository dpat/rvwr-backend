#!/usr/bin/env python3

from flup.server.fcgi import WSGIServer
from rvwr import rvwr


if __name__ == '__main__':
    rvwr.setup_logging(debug=False, verbose=True)
    app = rvwr.config_app('rvwr')
    rvwr.BPHandler.register_blueprints(app)
    rvwr.config_dabase(app)
    WSGIServer(app).run()
