from flask import Flask, render_template, request#, redirect, url_for
import sqlite3


app = Flask(__name__)
#x=0
#conn = sqlite3.connect("blog.db")
#p ="create table posts(post_id integer, post_title text, post_author text, post_content text);"
#comm = "create table comments(comment_id integer, comment_content text, comment_author text,p_id integer);"

#c = conn.cursor()
#c.execute(p)
#c.execute(comm)
#conn.commit();

@app.route("/")
def home():
    newpost = request.args.get ("new_post", None)
    title = request.args.get ("title", None)
    author = request.args.get ("author", None)
    post = request.args.get ("post", None)
    #make lists and play around with nested loops and loops.index
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    if newpost == "Post":
        q = "Insert Into posts Values('" + title + "','" + author + "','" + post + "');"
        c.execute(q)
        #x = x + 1
    #link =  '/'+ title + ''
    s = "Select post_title From posts"
    t = "Select post_author From posts"
    u = "Select post_content From posts"
    title_list = []
    author_list = []
    post_list = []
    titles = c.execute(s)
    title_list = [(str(x)[3:])[:-3] for x in titles]
    authors= c.execute(t)
    author_list = [(str(x)[3:])[:-3] for x in authors]
    posts= c.execute(u)            
    post_list = [(str(x)[3:])[:-3] for x in posts]
    conn.commit()
    print title_list
    print author_list
    print post_list
    return render_template ("index.html",
                            #ignore link
                            #link = link,
                            title_list = title_list,
                            author_list = author_list,
                            post_list = post_list)

@app.route("/<title>")
##check if title is unique
def new_post(title):
    author = "select author from posts"
    post = "select post from posts"
    return render_template ("post.html", title = title, author = author, post = post)
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=8888)
