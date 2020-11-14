from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Mugilan E.S.",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "April 23, 1999",
    },
    {
        "author": "Samantha",
        "title": "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "October 18, 2020",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run()