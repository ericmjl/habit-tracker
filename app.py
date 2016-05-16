from flask import Flask, render_template, request
from tinydb import TinyDB, Query

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
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
