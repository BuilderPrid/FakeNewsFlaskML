from flask import Blueprint, render_template,request,url_for,redirect,flash
from .predictors.d1 import predict
from flask_login import login_required,current_user
views = Blueprint('views',__name__)
from .models import Result
from . import db 
import json

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method=='POST':
        # raise KeyError

        title = request.form.get('news-title')
        text = request.form.get('news-text')
        publisher = request.form.get('publisher')
        result= predict(title,text,maxlen=1000)[0][0]
        print(result,'res')
        # print('url',red_url)
        return redirect(url_for('.result',result = result,title=title))
    else:
        return render_template('home.html',user =current_user)

@views.route('/features')
def features():
    return render_template('base.html',user=current_user)


@views.route('/history')
@login_required
def history():
    return render_template('history.html',user=current_user)

@views.route('/result',methods=['POST','GET'])
def result():
    return render_template('result.html',result=int(request.args['result']),title=request.args['title'],user=current_user)

@views.route('/saveResult',methods=['POST'])
def saveResult():
    data = json.loads(request.data)
    title=data['title']
    result=int(data['result'])
    newResult = Result(title=title,result=result,userId=current_user.id)
    db.session.add(newResult)
    db.session.commit()
    flash('Result saved',category='success')
    return ({})