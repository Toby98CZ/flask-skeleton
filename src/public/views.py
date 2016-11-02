"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template
from .forms import LogUserForm, FormularHodnota
from ..data.database import db
from ..data.models import LogUser, Databaze
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/formularhodnota', methods=['GET', 'POST'])
def formularhodnotanew():
    form = FormularHodnota()
    if form.validate_on_submit():
        Databaze.create(**form.data)
    return render_template("public/formular.tmpl", form=form)

@blueprint.route('/writetask', methods=['GET', 'POST'])
def WriteTaskLog():
    pole = db.session.query(Databaze).all()
    return render_template("public/writeTasks.tmpl", data=pole)

@blueprint.route('/smazat/<int:id>', methods=['GET', 'POST'])
def smazat(id):
    pole = db.session.query(Databaze).filter_by(Databaze.id==id).first()
    try:
        db.session.remove(pole)
    except:
        status=["Chyba","Error"]
        #return redirect(ListuserLog)
        return False
    return True