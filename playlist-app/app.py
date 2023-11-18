from flask import Flask, redirect, render_template, flash
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///jeffreyng'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"
app.debug=True
# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)
app.config['SQLALCHEMY_RECORD_QUERIES'] = True

@app.route("/")
def root():
    """Homepage: redirect to /playlists."""
    
    return redirect("/playlists")


##############################################################################
# Playlist routes
@app.route("/playlists", methods=['POST'])
def show_all_playlists():
    """Return a list of playlists."""
    

    return render_template("playlists.html")

@app.route("/playlists", methods=['GET'])
def get_all_playlists():
    """Return a list of playlists."""
    playlists=Playlist.query.all()

    return render_template("playlists.html", playlists=playlists)







@app.route("/playlists/<int:playlist_id>", methods=['GET', 'POST'])
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    playlist=Playlist.query.get_or_404(playlist_id)

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    return render_template('playlist.html', playlist=playlist)

@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK   
   
    form = PlaylistForm()
    if form.validate_on_submit():
        name= form.name.data
        description= form.description.data
        new_playlist= Playlist(name=name, description=description)
        db.session.add(new_playlist)
        db.session.commit()
        return redirect('/playlists')
    else:
        return render_template('new_playlist.html', form=form)

##############################################################################
# Song routes


@app.route("/songs", methods= ['GET', 'POST'])
def show_all_songs():
    """Show list of songs."""

    song = Song.query.all()
    return render_template("songs.html", song=song)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""
    canto =Song.query.get_or_404(song_id)
    return render_template('song.html', song=canto)
    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    form = SongForm()

    if form.validate_on_submit():
        title = form.title.data
        artist = form.artist.data
        mp3=form.mp3.data
        genre= form.genre.data
        year_released = form.year_released.data

        new_song=Song(title=title, artist=artist, mp3=mp3, genre=genre, year_released=year_released)
        db.session.add(new_song)
        db.session.commit()
        return redirect('/songs')
    else:    
        return render_template('new_song.html', form=form) 

@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist

    curr_on_playlist = PlaylistSong.filter(playlist_id= playlist_id)


    form.song.choices = ...

    if form.validate_on_submit():

          # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
        song = form.song.data
        
        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)
