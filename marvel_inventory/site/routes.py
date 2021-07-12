from flask import Blueprint, render_template
from flask_login.utils import login_required
"""
    Some arguments are specified when creating the Blueprint object.
    The first argument "site", is the blueprint name,
    which is used by Flask's routing mechanism.

    The second argument, __name__, is the Blueprint's import name,
    this is how flask locates the blueprint's resources.
"""

site = Blueprint("site", __name__, template_folder="site_templates")

@site.route("/")
def index():
    return render_template("index.html")

@site.route("/profile")
@login_required
def profile():
    return render_template("profile.html")