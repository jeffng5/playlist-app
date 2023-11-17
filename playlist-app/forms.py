"""Forms for playlist app."""

from wtforms import SelectField, StringField, FileField, DateField
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField('name of playlist')
    description= StringField('description of playlist')

class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form

    title = StringField('song title')
    mp3 = FileField('mp3 file')
    artist = StringField('artist')
    genre = SelectField('genre', choices =[('rock','rock'), ('jazz','jazz'), ('pop','pop'), ('classical','classical'), ('hiphop','hiphop'), ('soundtrack','soundtrack'), ('blues','blues')])
    year_released = DateField('year released')








# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
