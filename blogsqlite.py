import sqlite3

conn = sqlite3.connect("blog.db")

p = "create table posts(post_id integer, post_title text, post_author text, post_content text); create table comments(comment_id integer, comment_content text, comment_author texr,p_id integer);"

c = conn.cursor()
c.execute(p)
conn.commit();
