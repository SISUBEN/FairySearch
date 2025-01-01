CREATE TABLE IF NOT EXISTS user_action (
    user_id INT NOT NULL,
    video_id INT NOT NULL,
    is_liked BOOLEAN NOT NULL,
    is_favourite BOOLEAN NOT NULL,
    is_coin BOOLEAN NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
);