
CREATE TABLE IF NOT EXISTS users (
                        uid INTEGER PRIMARY KEY AUTOINCREMENT,
                        username CHAR(32) NOT NULL,
                        password CHAR(32) NOT NULL,
                        token VARCHAR(32) NOT NULL
                    );

CREATE TABLE IF NOT EXISTS search_history (
                        uuid CHAR(33) PRIMARY KEY,
                        vid INTEGER NOT NULL,
                        userid INTEGER NOT NULL,
                        title VARCHAR(32) NOT NULL,
                        timestamp INTEGER NOT NULL,
                        duration INTEGER NOT NULL,
                        FOREIGN KEY (userid) REFERENCES users(uid)
                    );