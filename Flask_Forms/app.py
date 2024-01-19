from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    
    breed = StringField("What Breed are you?")
    submit = SubmitField('Submit')
    
@app.route('/', methods=["GET",'POST'])
def index():
    
    breed = False
    form = InfoForm()
    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ''
    return render_template('home.html',form=form,breed=breed)

if __name__ == '__main__':
    app.run(debug=True)