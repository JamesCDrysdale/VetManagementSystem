from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client import Client
from repositories import client_repository

clients_blueprint = Blueprint("clients", __name__)

################
###  CREATE  ###
################

# CREATE NEW CLIENT
@clients_blueprint.route("/clients/new", methods=['GET'])
def new_client():
    clients = client_repository.select_all()
    return render_template("clients/new.html", all_clients = clients)


# POST NEW CLIENT TO DB
@clients_blueprint.route("/clients", methods=['POST'])
def create_client():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    client = Client(first_name, last_name, email, phone)
    client_repository.save(client)
    return redirect('/clients')


################
###   READ   ###
################

# GET ALL CLIENTS
@clients_blueprint.route("/clients")
def clients():
    clients = client_repository.select_all()
    return render_template("clients/index.html", all_clients = clients)

# GET SELECTED CLIENT
@clients_blueprint.route("/clients/<id>", methods=['GET'])
def show_client(id):
    client = client_repository.select(id)
    return render_template('clients/show.html', client = client)


################
###  UPDATE  ###
################


################
###  DELETE  ###
################