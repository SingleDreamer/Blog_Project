from flask import Flask, render_template, request#, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    newpost = request.args.get ("new_post", None)
    title = request.args.get ("title", None)
    author = request.args.get ("author", None)
    post = request.args.get ("post", None)
    if newpost == "Post":
        link =  '/'+ title + ''
        return render_template ("index.html", 
                                link = link,
                                title = title,
                                author = author,
                                post = post)
    else:
        return render_template ("index.html", posts = "")

@app.route("/<title>")
def new_post(title):
    return title + "yolo"
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=8888)
