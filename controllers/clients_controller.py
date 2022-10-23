from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.client import Client
from repositories import client_repository

clients_blueprint = Blueprint("clients", __name__)

@clients_blueprint.route("/clients")
def tasks():
    clients = client_repository.select_all()
    return render_template("clients/index.html", all_clients = clients)