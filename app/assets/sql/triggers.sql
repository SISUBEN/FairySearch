-- after-delete trigger
CREATE TRIGGER IF NOT EXISTS videos_ad AFTER DELETE ON videos BEGIN
DELETE FROM videos_fts
WHERE
    rowid = old.video_id;

END;
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
-- after-update trigger
CREATE TRIGGER IF NOT EXISTS videos_au AFTER
UPDATE ON videos BEGIN
UPDATE videos_fts
SET
    video_title = new.video_title,
    video_tags = new.video_tags,
    video_desc = new.video_desc
WHERE
    rowid = old.video_id;

END;