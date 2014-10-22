from flask import Flask, render_template, request#, redirect, url_for
import sqlite3

app = Flask(__name__)
#x=0
conn = sqlite3.connect("blog.db")
p ="create table posts(post_id integer, post_title text, post_author text, post_content text);"
comm = "create table comments(comment_id integer, comment_content text, comment_author text,p_id integer);"

c = conn.cursor()
#c.execute(p)
#c.execute(comm)
conn.commit();

@app.route("/")
def home():
    newpost = request.args.get ("new_post", None)
    title = request.args.get ("title", None)
    author = request.args.get ("author", None)
    post = request.args.get ("post", None)
    #make lists and play around with nested loops and loops.index
    if newpost == "Post":
        link =  '/'+ title + ''
        conn = sqlite3.connect("blog.db")
        c = conn.cursor()
        q = "Insert Into posts Values(1,'" + title + "','" + author + "','" + post + "');"
        #x = x + 1
        s = "Select post_title From posts"
        t = "Select post_author From postxs"
        u = "Select post_content From posts"
        c.execute(q)
        title_list = c.execute(s)
        author_list = c.execute(t)
        post_list = c.execute(u)            
        conn.commit()
        return render_template ("index.html",
                                #ignore link
                                link = link,
                                title = title_list,
                                author = author_list,
                                post = post_list)
    else:
        return render_template ("index.html")

@app.route("/<title>")
##check if title is unique
def new_post(title):
    author = "select author from posts"
    post = "select post from posts"
    return render_template ("post.html", title = title, author = author, post = post)
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=8888)
