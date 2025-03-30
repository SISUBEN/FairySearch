INSERT INTO
    videos_fts (rowid, video_title, video_tags, video_desc)
SELECT
    video_id,
    video_title,
    video_tags,
    video_desc
FROM
    videos;