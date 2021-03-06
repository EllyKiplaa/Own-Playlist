from flask_wtf import FlaskForm
from  wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PlaylistForm(FlaskForm):
    """
    Class to create forms for creating playlists
    """
    name = StringField("Playlist Name", validators=[Required()])
    submit = SubmitField("Submit")
    

# class UpdateProfile (FlaskForm):
#     bio = TextAreaField("Tell us about yourself", validators = [Required()])
#     submit = SubmitField ("Submit")
    