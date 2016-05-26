from flask import Flask, render_template, request
from tinydb import TinyDB, Query
from datetime import datetime, timedelta

import os
import os.path as op

# Pre-initialization checks
# 1. Initialize database.

# Initialize app
app = Flask(__name__)
# db = TinyDB(db_path)


@app.route('/')
def main():
    """
    The main page. Lists a calendar view (4 weeks).
    """

    today = datetime.today()
    dates = [today - timedelta(2),
             today - timedelta(1),
             today,
             today + timedelta(1),
             today + timedelta(2)]

    return render_template('index.html',
                           dates=dates,
                           today=today)

if __name__ == '__main__':
    app.run(debug=True)
