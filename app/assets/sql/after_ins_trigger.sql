-- after-insert trigger
CREATE TRIGGER IF NOT EXISTS videos_ai AFTER INSERT ON videos BEGIN
INSERT INTO
    videos_fts (rowid, video_title, video_tags, video_desc)
VALUES
    (
        new.video_id,
        new.video_title,
        new.video_tags,
        new.video_desc
    );

END;