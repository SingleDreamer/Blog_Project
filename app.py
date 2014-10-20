from flask import Flask, render_template, request#, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    newpost = request.args.get ("new_post", None)
    title = request.args.get ("title", None)
    author = request.args.get ("author", None)
    post = request.args.get ("post", None)
    if newpost == "Post":
        text =  title + "<br>" + author + "<br>" + post
        return render_template ("index.html", posts = text)
    else:
        return render_template ("index.html", posts = "")

@app.route("/<title>")
def new_post(title):
    return title + "yolo"
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=8888)
