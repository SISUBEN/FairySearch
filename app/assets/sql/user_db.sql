CREATE TABLE
    IF NOT EXISTS users (
        uid INTEGER PRIMARY KEY AUTOINCREMENT,
        username CHAR(32) NOT NULL,
        password CHAR(32) NOT NULL,
        token VARCHAR(32) NOT NULL
    );