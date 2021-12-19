DROP TABLE IF EXISTS image;

CREATE TABLE image (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  path TEXT UNIQUE NOT NULL,
  description TEXT NOT NULL
);