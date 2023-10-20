#!/usr/bin/python3

from app import app
from routes import main
import sys


app.register_blueprint(main)

if __name__ == '__main__':
    app.run(host='172.31.28.152', port=3000)
    sys.exit(0)

    