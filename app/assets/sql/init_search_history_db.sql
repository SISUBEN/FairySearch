CREATE TABLE
    IF NOT EXISTS search_history (
        uuid CHAR(33) PRIMARY KEY,
        vid INTEGER NOT NULL,
        userid INTEGER NOT NULL,
        title VARCHAR(32) NOT NULL,
        timestamp INTEGER NOT NULL,
        duration INTEGER NOT NULL,
        FOREIGN KEY (userid) REFERENCES users (uid)
    );