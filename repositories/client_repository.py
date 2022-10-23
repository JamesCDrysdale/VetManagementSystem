from db.run_sql import run_sql

from models.client import Client

def save(client):
    sql = "INSERT INTO clients (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [client.first_name, client.last_name, client.phone, client.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    client.id = id
    return client


def select_all():
    clients = []

    sql = "SELECT * FROM clients"
    results = run_sql(sql)

    for row in results:
        client = Client(row['first_name'], row['last_name'], row['phone'], row['email'], row['id'] )
        clients.append(client)
    return clients