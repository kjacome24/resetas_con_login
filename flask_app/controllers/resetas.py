from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.reseta import Reseta


@app.route('/dashboard')
def dashboard():
    if session.get('id') == None:
        return redirect('/')
    resetas = Reseta.get_all_with_owner()
    print(resetas)
    return render_template('dashboard.html',resetas = resetas )

