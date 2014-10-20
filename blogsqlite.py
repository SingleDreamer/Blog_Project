import sqlite3

conn = sqlite3.connect("blog.db")

p = "create table posts(post_id integer, title text, content text);
create table comments(comment_id integer, content text, p_id integer);"

c = conn.cursor()
c.execute(p)
conn.commit();
