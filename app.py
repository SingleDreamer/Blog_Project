from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    newpost = request.args.get ("new_post", None)
    if newpost == "New Post":
        return redirect (url_for('new_post'))
    else:
        return render_template ("index.html")

@app.route("/new_post")
def new_post():
    return "yolo"
    
if __name__ == "__main__":
    app.debug = True
    app.run()
        #host="0.0.0.0",port=8888)
