from db.run_sql import run_sql

from models.client import Client

# CREATE
def save(client):
    sql = "INSERT INTO clients (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [client.first_name, client.last_name, client.email, client.phone]
    results = run_sql(sql, values)
    id = results[0]['id']
    client.id = id
    return client

#  READ
def select_all():
    clients = []

    sql = "SELECT * FROM clients"
    results = run_sql(sql)

    for row in results:
        client = Client(row['first_name'], row['last_name'], row['email'], row['phone'], row['id'] )
        clients.append(client)
    return clients

def select(id):
    client = None
    sql = "SELECT * FROM clients WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        client = Client(result['first_name'], result['last_name'], result['email'], result['phone'], result['id'] )
    return client

# UPDATE
def update(client):
    sql = "UPDATE clients SET (first_name, last_name, email, phone) = (%s, %s, %s, %s) WHERE id = %s"
    values = [client.first_name, client.last_name, client.email, client.phone, client.id]
    run_sql(sql, values)

# DELETE

def delete_all():
    sql = "DELETE  FROM clients"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM clients WHERE id = %s"
    values = [id]
    run_sql(sql, values)