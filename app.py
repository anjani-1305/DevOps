import os

from flask import Flask, render_template 

app = Flask(__name__)

color = os.environ.get('APP_COLOR')

@app.route('/')
def main():
    print(color)
    return render_template('D:\Kuber\Docker\hello.html' , colour=color)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
    