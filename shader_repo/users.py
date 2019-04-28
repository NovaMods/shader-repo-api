"""Basic API for user-related operations
"""

from datetime import date
import functools
import json

from flask import (
    Blueprint, g, redirect, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from shader_repo import util

insert_user_statement = """
INSERT INTO users (email, username, password_hashed, skype_name, twitter_handle, discord_name, mojang_name, 
                   minecraftforum_name, personal_website, join_date)
VALUES (%(email)s, %(username)s, %(password_hashed)s, %(skype_name)s, %(twitter_handle)s, 
        %(discord_name)s, %(mojang_name)s, %(minecraftforum_name)s, %(personal_website)s, %(join_date)s)
"""

find_user_by_username_statement = """
SELECT * FROM users WHERE username=%(username)s
"""

find_user_by_email_statement = """
SELECT * FROM users WHERE email=%(email)s
"""

bp = Blueprint('users', __name__, url_prefix='/users')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('users.login'))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        with util.connection:
            with util.connection.cursor() as cursor:
                cursor.execute('SELECT * FROM users WHERE email=%(email)s', {'email': user_id})
                g.user = cursor.fetchone()


@bp.route('', methods=['POST'])
def add_user():
    """Add a new user to the database

    A user must be provided in JSON in the body of a POST request. Email, username, and password are required. You may
    provide social media usernames, like Skype or Discord or Twitter, but those may be safely omitted

    This function checks that the email, username, and password are all present. It then checks that no existing users
    are using the username or email that you want to user. Assuming all checks pass, a new user is created - with the
    hashed password stored in the DB
    """

    if request.headers['content-type'] != 'application/json':
        return 'Must send a JSON request', 400

    new_user = dict()

    data = json.loads(request.data)

    required_fields = ['email', 'username', 'password']
    optional_fields = ['skype_name', 'twitter_handle', 'discord_name', 'mojang_name', 'minecraftforum_name',
                       'personal_website']

    missing_fields = list()
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)

    if len(missing_fields) != 0:
        return f"Missing required fields {','.join(missing_fields)}", 400

    new_user['email'] = data['email']
    new_user['username'] = data['username']
    new_user['password_hashed'] = generate_password_hash(data['password'])
    new_user['join_date'] = date.today()

    for field in optional_fields:
        if field in data:
            new_user[field] = data[field]

        else:
            new_user[field] = None

    with util.connection:
        with util.connection.cursor() as cursor:
            cursor.execute(find_user_by_username_statement, {'username': new_user['username']})
            if cursor.rowcount != 0:
                return f"A user with username {new_user['username']} already exists", 400

            cursor.execute(find_user_by_email_statement, {'email': new_user['email']})
            if cursor.rowcount != 0:
                return f"A user with email {new_user['email']} already exists", 400

            cursor.execute(insert_user_statement, new_user)

            return 'OK', 200


@bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    with util.connection:
        with util.connection.cursor() as cursor:
            cursor.execute(find_user_by_email_statement, {'email': email})
            if cursor.rowcount == 0:
                return 'Incorrect username or password', 400

            user = cursor.fetchone()

            if not check_password_hash(user['password'], password):
                return 'Incorrect username or password', 400

            session.clear()
            session['user_id'] = email

            return 'Ok', 200


# def activate_user():


# def edit_user():


# def delete_user():
