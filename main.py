from app.reports.api import api
from flask import Flask

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

# @app.before_request
# def auth_user():
#     pass
#
# @app.after_request
# def add_header(response):
#     pass


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


@app.errorhandler(500)
def server_error(e):
    """Return a custom 500 error."""
    return 'Error while serving request', 418
