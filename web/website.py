from flask import Flask, render_template, url_for
from pymongo import MongoClient

from database.requests.get import many_report
from config_reader import config

app = Flask(__name__, template_folder='html')
cluster = MongoClient(config.DATABASE_URL.get_secret_value())
mdb = cluster.games

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/chart')
def menu_chart():
    return render_template("menu_chart.html")


@app.route('/chart/report')
def chart_report():
    reports = mdb.report.find({})
    for report in reports:
        print(report)
    return render_template("chart/report.html")


@app.route('/form_create')
def menu_create():
    return render_template("menu_create.html")


@app.route('/form_create/ability')
def create_ability():
    return render_template("create/ability_create.html")


def start_website():
    app.run(debug=True)

if __name__ == '__main__':
    start_website()