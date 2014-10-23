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

    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    if newpost == "Post":
        q = "Insert Into posts Values('" + title + "','" + author + "','" + post + "');"
        c.execute(q)
        #x = x + 1
    #link =  '/'+ title + ''
    s = "Select title From posts"
    t = "Select author From posts"
    u = "Select content From posts"
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
def post(title):
    t = title.replace ("+", " ")
    nc = request.args.get ("new_comment", None)
    commentor = request.args.get ("commentor", None)
    comment = request.args.get ("comment", None)
    print commentor
    print comment
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    if nc == "Post": 
        q = "Insert Into comments Values('" + t + "','" + commentor + "','" + comment + "');"
        c.execute(q)
        

    commentor_list = []
    comment_list = []
    
    a = "select author from posts where title = '" + t + "'"
    author = c.execute (a)
    authorstr = author= [(str(x)[3:])[:-3] for x in author]
    print authorstr
    p = "select content from posts where title = '" + t + "'"
    post = c.execute (p)
    poststr = [(str(x)[3:])[:-3] for x in post]
    print poststr
    
    x = "select commentor from comments where title == '" + t + "';"        
    y = "select comment from comments where title == '" + t + "';"
    
    commentors = c.execute (x)
    commentor_list = [(str(x)[3:])[:-3] for x in commentors]
    comments = c.execute (y)
    comment_list =  [(str(x)[3:])[:-3] for x in comments]
    conn.commit()

    print commentor_list
    print comment_list


    return render_template ("post.html", 
                            title = t, 
                            author = authorstr[0], 
                            post = poststr[0],
                            commentor_list = commentor_list, 
                            comment_list = comment_list)
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=8888)
