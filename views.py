#!/usr/bin/env python3

from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html", name="default")


# use route as key as variable for html
@views.route("/profile/<username>")
def short_profile(username):
    return render_template("index.html", name=username)


# use query parameters on route as variable for html
@views.route("/profile")
def profile():
    args = request.args
    color = args.get('color')
    name = args.get('name')
    return render_template("index.html", name=name, color=color)


# send json upon route request
@views.route("/json")
def get_json():
    return jsonify({"name": "nik", "favorite color": "red"})


# send json data that is deplayed
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


# redirect to home
@views.route("/go_to_home")
def go_to_home():
    return redirect(url_for("views.home"))
