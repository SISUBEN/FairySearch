CREATE TABLE IF NOT EXISTS videos (
                    video_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    video_title VARCHAR(50),
                    video_cover_path TEXT,
                    video_time_sec FLOAT,
                    video_type TEXT,
                    video_tags TEXT,
                    video_desc TEXT
                );