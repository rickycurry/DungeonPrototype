CREATE TABLE treasures (
  id SERIAL PRIMARY KEY NOT NULL,
  coin BOOLEAN,
  gem BOOLEAN,
  jewelry BOOLEAN,
  valuable BOOLEAN,
  magic_item BOOLEAN,
  potion BOOLEAN,
  scroll BOOLEAN
);