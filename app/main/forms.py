from flask_wtf import FlaskForm
from  wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class OwnPlaylistForm(FlaskForm):
    """
    Class to create forms for creating playlists
    """
    name = StringField("Playlist Name", validators=[Required()])
    submit = SubmitField("Submit")
    

class UpdateProfile (FlaskForm):
    bio = TestAreaField("Tell us about yourself", validators = [Required()])
    submit = Submit ("Submit")
    