from flask import Flask, url_for

from users import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    # Show the main page of the shader repo. It should display the most popular shaderpacks of the month in a grid view
    return 'Hello World!'


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/site-map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        url = url_for(rule.endpoint, **(rule.defaults or {}))
        print(url)
        links.append(url)

    return 200


if __name__ == '__main__':
    from . import users
    app.register_blueprint(users.bp)

    app.run()
