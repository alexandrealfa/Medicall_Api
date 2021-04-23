import os

from app import create_app

env = os.getenv('FLASK_ENV') or 'test'

app = create_app(env)
if __name__ == "__main__":
    app.run()