from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# import secrets
# secrets.token_hex(16)
app.config["SECRET_KEY"] = "ecc3c74cde310eb6fc1d801b266aa3c8"

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


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register Form", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login Form", form=form)


if __name__ == "__main__":
    app.run()