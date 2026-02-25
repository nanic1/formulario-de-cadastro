from flask import Blueprint, render_template, request
from .models import User
from . import db

main = Blueprint("main", __name__)

@main.route("/")
def root():
    return render_template("cadastro.html")

@main.route("/registro", methods=["POST"])
def registro():
    name = request.form.get("firstname")
    lastname = request.form.get("lastname")
    email = request.form.get("email")
    number = request.form.get("number")
    password = request.form.get("password")
    gender = request.form.get("gender")

    novo_usuario = User(
        name=name,
        lastname=lastname,
        email=email,
        number=number,
        password=password,
        gender=gender
    )

    db.session.add(novo_usuario)
    db.session.commit()

    return render_template("cadastro.html", sucess=True)