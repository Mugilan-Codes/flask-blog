# Blog

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
  from flaskblog import User, Post
  user_1 = User(username="Mugilan", email="mugilancodes@gmail.com", password="password")
  db.session.add(user_1)
  user_2 = User(username="Jayashree", email="jay@gmail.com", password="password")
  db.session.add(user_2)
  db.session.commit()
  User.query.all() # to get all users
  User.query.first() # to get first user
  User.query.filter_by(username="Mugilan").all() # filtering the results
  user = User.query.filter_by(username="Mugilan").first() # get the first result of the filter
  user
  user.id
  user = User.query.get(1)
  user.posts
  post_1 = Post(title="Blog 1", content="First Post Content!", user_id=user.id)
  post_2 = Post(title="Blog 2", content="Second Post Content!", user_id=user.id)
  db.session.add(post_1)
  db.session.add(post_2)
  db.session.commit()
  user.posts
  for post in user.posts:
    print(post.title)
  post = Post.query.first()
  post
  post.user_id
  post.author
  db.drop_all()
  ```
