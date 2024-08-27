
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    brief TEXT NOT NULL,
    content BLOB,
    img_path varchar(255),
    post_name varchar(255),
    views INTEGER

);