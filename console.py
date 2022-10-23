import pdb
from models.client import Client


import repositories.client_repository as client_repository

client1 = Client("Jack", "Jarvis", "jackjarvis@coderdude.com", "01875 567 654")
# client_repository.save(client1)

client_repository.select_all()


pdb.set_trace()