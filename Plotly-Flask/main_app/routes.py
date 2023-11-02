from flask import Blueprint, render_template,redirect

server_bp = Blueprint('main', __name__)


@server_bp.route('/')
def index():
    # Redirect to '/app_1/' when the root URL is accessed
    return redirect('/app_1/')

@server_bp.route('/app_1/')
def app_1_template():
    return render_template('dash.html', dash_url='/app_1_raw_dash/')


@server_bp.route('/app_2/')
def app_2_template():
    return render_template('dash.html', dash_url='/app_2_raw_dash/')

