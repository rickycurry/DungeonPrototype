CREATE TABLE contents (
  id SERIAL PRIMARY KEY NOT NULL,
  feature VARCHAR(255) NOT NULL,
  atmosphere VARCHAR(255) NOT NULL,
  monster BOOLEAN,
  treasure BOOLEAN,
  special BOOLEAN
);

CREATE TABLE adjectives (
  id SERIAL PRIMARY KEY NOT NULL,
  word VARCHAR(255)
);