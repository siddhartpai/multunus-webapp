from flask.ext.wtf import Form, TextField, BooleanField
from flask.ext.wtf import Required

class nameForm(Form):
    screenName = TextField('screenName', validators = [Required()])
    def getScreenName():
	return screenName


