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