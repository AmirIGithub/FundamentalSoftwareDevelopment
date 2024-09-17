"""The backend for Burger Order."""

from flask import Flask, render_template, url_for, request, redirect, session
import os
import requests

app = Flask(__name__)


# render index.html (home page) when user on home route (website.com/)
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)