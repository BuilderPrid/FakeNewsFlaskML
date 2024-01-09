from flask import Blueprint, render_template,request,url_for,redirect,flash
from .predictors.d1 import predict
from flask_login import login_required,current_user
views = Blueprint('views',__name__)

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
        return redirect(url_for('.result',result = result))
    else:
        return render_template('home.html',user =current_user)

@views.route('/features')
def features():
    return render_template('base.html')


@views.route('/history')
def history():
    return 'history'

@views.route('/result')
def result():
    return render_template('result.html',result=request.args['result'],user=current_user)
