from flask import render_template

from watchlist import app


@app.errorhandler(400)
def bad_request(e):
    return render_template("error/400.html"), 400
