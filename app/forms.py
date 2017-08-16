from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Required

class LoginForm(Form):
    openid = TextField('openid', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)
    #email = StringField('Email', validators=[Required(), Length(1,64), Email()])
    #password = PasswordField('Password', validators=[Required()])
    #remember_me = BooleanField('Keep me login')
    #submit = SubmitField('LogIn')
    
