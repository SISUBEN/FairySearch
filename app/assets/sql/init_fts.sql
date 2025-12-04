CREATE VIRTUAL TABLE IF NOT EXISTS videos_fts USING fts5 (video_id, video_title, video_tags, video_desc);

INSERT INTO
    videos_fts (video_id, video_title, video_tags, video_desc)
SELECT
    video_id,
    video_title,
    video_tags,
    video_desc
FROM
    videos;