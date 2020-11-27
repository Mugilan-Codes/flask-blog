# Flask-Blog

> By [Mugilan](https://github.com/Mugilan-Codes)

## Todo

- Cleanup old Profile Pics
- Add and delete posts
- Change to MongoDB instead of SQLAlchemy
- Paginate Posts to Home page
- Refactor Code

## How to Run

- Create a Virtual Environment
  
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

- Install required packages

  ```bash
  pip install -r requirements.txt
  ```

- Run the Flask app

  ```bash
  flask run
  ```
  
- migrate db

  ```py
  from flaskblog import db
  db.create_all()
  ```

> [Flask-Blog Github Link](https://github.com/Mugilan-Codes/flask-blog)
