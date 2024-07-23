from flask_wtf import FlaskForm
from wtforms import StringField , BooleanField, IntegerField , SubmitField
from wtforms.validators import DataRequired , URL, Optional, NumberRange

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators = [DataRequired()])
    species = StringField('Pet Species', validators = [DataRequired()])
    photo_url = StringField('Photo URL', validators=[Optional(), URL(message="Must be a valid URL")])
    age = IntegerField('Pet Age' , validators = [Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField('Additional Information')
    available = BooleanField('Available')
    submit = SubmitField('Submit')