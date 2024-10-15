import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    app_name = os.getenv('APP_NAME', 'My Simple Flask App')
    return f"Hello from {app_name}!"

if __name__ == '__main__':
    app.run()
