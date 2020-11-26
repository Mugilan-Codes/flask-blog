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
  ```
