from flask_wtf import Form
from wtforms import StringField, FieldList, FormField, TextField
from wtforms.validators import DataRequired

class RuleForm(Form):
    source = StringField('source', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    port = StringField('port', validators=[DataRequired()])

