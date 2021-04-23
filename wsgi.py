import os

from app import create_app

env = os.getenv('FLASK_ENV')

app = create_app(env)
if __name__ == "__main__":
    app.run("0.0.0.0")
