import os
import eyed3 as eyed3

dir_path = '/home/parth/Music/tagging'
os.chdir(dir_path)

for song in os.listdir(dir_path):
    song_name, song_ext = os.path.splitext(song)
    song_artist, song_title = song_name.split(' - ')

    tag_song = eyed3.load(song)
    tag_song.tag.artist = unicode(song_artist, "utf-8")
    tag_song.tag.title = unicode(song_title, "utf-8")
    tag_song.tag.save()
    
    
