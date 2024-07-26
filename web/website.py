from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='html')

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/form_create')
def create():
    return render_template("menu_create.html")

@app.route('/form_create/ability')
def create_ability():
    return render_template("create/ability_create.html")


def start_website():
    app.run(debug=True)

if __name__ == '__main__':
    start_website()