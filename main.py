import os
from OraApp import create_app

secret_key = os.environ.get('SECRET_KEY')

# initializing flask app
app = create_app()

if __name__ == "__main__":
    app.run()