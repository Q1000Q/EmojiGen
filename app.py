from flask import Flask, render_template
from os import getenv
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

load_dotenv()

@app.route('/', methods=['GET'])
def method_name():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)