CREATE TABLE
    IF NOT EXISTS users (
        uid INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(32) NOT NULL,
        password VARCHAR(32) NOT NULL,
        token VARCHAR(32) NOT NULL
    );