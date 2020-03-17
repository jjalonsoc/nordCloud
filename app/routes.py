from flask import render_template, request
from app import app
from .util.link_stations_optimizer import most_suitable_link_station


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nordcloud'}
    posts = [
        {
            'author': {'username': 'Jose Joaquin '},
            'body': 'Technical task!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/links-point', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        stations_list = request.form.get('stations_list')
        point = request.form['point']
        opt_link = most_suitable_link_station(eval(point), eval(stations_list))
        return render_template('solution.html', title="Challenge", solution_str=opt_link)

    return render_template('task.html', title='Challenge-Input')
