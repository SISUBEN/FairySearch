-- after-delete trigger
CREATE TRIGGER IF NOT EXISTS videos_ad AFTER DELETE ON videos BEGIN
DELETE FROM videos_fts
WHERE
    rowid = old.video_id;

END;