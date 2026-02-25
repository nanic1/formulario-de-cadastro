from flask import Blueprint, render_template, request, redirect, url_for, flash
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
    confirmpassword = request.form.get("Confirmpassword")
    gender = request.form.get("gender")

    if not name or not lastname or not email or not number or not password or not confirmpassword or not gender:
        flash("Todos os campos são obrigatórios.")
        return redirect(url_for("main.root"))

    if password != confirmpassword:
        flash("As senhas não coincidem.")
        return redirect(url_for("main.root"))

    try:
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

        flash("Cadastro realizado com sucesso!")
    
    except:
        db.session.rollback()
        flash("Erro ao cadastrar. Tente novamente.")
        
    return redirect(url_for("main.root"))