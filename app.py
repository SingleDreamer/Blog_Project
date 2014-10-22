from flask import Flask, render_template, request#, redirect, url_for
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("blog.db")
q = "create table posts(title text)"
'''c=conn.cursor()
c.execute(q)
'''

@app.route("/")
def home():
    newpost = request.args.get ("new_post", None)
    title = request.args.get ("title", None)
    author = request.args.get ("author", None)
    post = request.args.get ("post", None)
    #make lists and play around with nested loops and loops.index
    if newpost == "Post":
        link =  '/'+ title + ''

        #q = "Insert Into posts Values(" + title +");"
        #c.execute(q)
        #conn.commit()
        return render_template ("index.html", 
                                link = link,
                                title = title,
                                author = author,
                                post = post)
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
