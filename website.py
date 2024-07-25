from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='web')

@app.route('/')
def home():
    return render_template("main.html")

def start_website():
    app.run(debug=True,)

if __name__ == '__main__':
    start_website()