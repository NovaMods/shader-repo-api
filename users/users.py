"""Basic API for user-related operations
"""

from datetime import date

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

import util


insert_user_statement = """
INSERT INTO users (email, username, password_hashed, skype_name, twitter_handle, discord_name, mojang_name, 
                   minecraftforum_name, personal_website, join_date)
VALUES (%(email)s, %(username)s, %(password_hash)s, %(skype_name)s, %(twitter_handle)s, 
        %(discord_name)s, %(mojang_name)s, %(minecraftforum_name)s, %(website)s, %(join_date)s)
"""


@app.route('/user', methods=['POST'])
def add_user():
    """Add a new user to the database
    """
    if request.headers['content-type'] != 'application/json':
        return 'Must send a JSON request', 400

    new_user = dict()

    data = request.data
    new_user['email'] = data['email']
    new_user['username'] = data['username']
    new_user['password_hashed'] = generate_password_hash(data['password'])
    new_user['join_date'] = date.today()

    optional_fields = ['skype_name', 'twitter_handle', 'discord_name', 'mojang_name', 'minecraftforum_name',
                       'personal_website']

    for field in optional_fields:
        if field in data:
            new_user[field] = data[field]

    with util.connection:
        with util.connection.cursor() as cursor:
            cursor.execute(insert_user_statement, new_user)
            cursor.commit()

            return 'OK', 200


# def activate_user():


# def edit_user():


# def delete_user():
