"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Playlist(db.Model):
    """Playlist."""

    __tablename__ = 'playlists'
    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement= True)
    name = db.Column(db.String(50),
                    nullable = False)
    description = db.Column(db.String(90),
                    nullable = False)
    # ADD THE NECESSARY CODE HERE

class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'
    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String,
                    nullable= False)
    artist = db.Column(db.String,
                    nullable=False)
    mp3 = db.Column(db.String,
                    nullable = True)
    genre = db.Column(db.String,
                      nullable= False)
    year_released = db.Column(db.Integer,
                              nullable = True)
    # ADD THE NECESSARY CODE HERE

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'playlistsongs'
    id = db.Column(db.Integer,
                    primary_key=True,
                        autoincrement=True)
    playlist_id= db.Column(db.Integer,
                    db.ForeignKey('playlists.id'))
    song_id = db.Column(db.Integer,
                    db.ForeignKey('songs.id'))

    
# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
