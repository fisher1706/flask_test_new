from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField("E-mail: ", validators=[Email("Incorrect e-mail")])
    psw = PasswordField("Password: ", validators=[DataRequired(), Length(min=4, max=100,
                                                                         message="must be between 4 and 100")])
    remember = BooleanField("Remember", default=False)
    submit = SubmitField("Enter")


class RegisterForm(FlaskForm):
    name = StringField("Name: ", validators=[Length(min=4, max=100, message="must be between 4 and 100")])
    email = StringField("E-mail: ", validators=[Email("Incorrect e-mail")])
    psw = PasswordField("Password: ", validators=[DataRequired(),
                                                  Length(min=4, max=100, message="must be between 4 and 100")])

    psw2 = PasswordField("Repeat Password: ", validators=[DataRequired(), EqualTo('psw', message="Password mismatch")])
    submit = SubmitField("Registration")
