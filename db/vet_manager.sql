DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS animals;

CREATE TABLE clients (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  email VARCHAR(255),
  phone VARCHAR(255)
);

-- CREATE TABLE vets (
--   id SERIAL PRIMARY KEY,
--   first_name VARCHAR(255),
--   last_name VARCHAR(255),
--   salary INT
-- );

-- CREATE TABLE animals (
--   id SERIAL PRIMARY KEY,
--   animal_name VARCHAR(255),
--   species VARCHAR(255),
--   dob DATE,
--   treatment_notes VARCHAR(255),
--   client_id INT NOT NULL REFERENCES clients(id),
--   vet_id INT REFERENCES vets(id)
-- );