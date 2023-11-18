from models import Playlist, Song, PlaylistSong, db
from app import app

db.drop_all()
db.create_all()

p1= Playlist(name='rock classics', description='favorite rock tracks of all time')
p2= Playlist(name='car ride music', description='favorite tracks to vibe to while driving')

s1=Song(title='Basketcase', artist='Green Day', genre= 'rock', year_released= '1994')
s2=Song(title= 'Meltaway', artist= 'Mariah Carey', genre = 'soft rock', year_released= '1998')


db.session.add(p1)
db.session.add(p2)
db.session.add(s1)
db.session.add(s2)

db.session.commit()

