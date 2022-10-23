from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client import Client
from repositories import client_repository

clients_blueprint = Blueprint("clients", __name__)

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