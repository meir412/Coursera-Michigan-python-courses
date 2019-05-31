import xml.etree.ElementTree as ET
import sqlite3

db_connection = sqlite3.connect('tracks.sqlite')
db_handler = db_connection.cursor()

db_handler.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

file_name = 'Library.xml'

parsed_xml_data = ET.parse(file_name)

def xml_lookup(track, key):
    found = False
    for child in track:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

all_tracks_data = parsed_xml_data.findall('dict/dict/dict')

for track_data in all_tracks_data:

    if xml_lookup(track_data,'Track ID') is None:
        continue

    name = xml_lookup(track_data, 'Name')
    artist = xml_lookup(track_data, 'Artist')
    album = xml_lookup(track_data, 'Album')
    count = xml_lookup(track_data, 'Play Count')
    rating = xml_lookup(track_data, 'Rating')
    length = xml_lookup(track_data, 'Total Time')

    if name is None or artist is None or album is None:
        continue

    db_handler.execute('''
    INSERT OR IGNORE INTO Artist (name)
    VALUES (?)''', (artist, ))

    db_handler.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = db_handler.fetchone()[0]

    db_handler.execute('''
    INSERT OR IGNORE INTO Album (title, artist_id)
    VALUES (?, ?)''', (album, artist_id))

    db_handler.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = db_handler.fetchone()[0]

    db_handler.execute('''
    INSERT OR REPLACE INTO Track
    (title, album_id, len, rating, count)
    VALUES (?, ?, ?, ?, ?)''', (name, album_id, length, rating, count))


db_connection.commit()
db_connection.close()

# first_track = all_tracks_data[0]
#
# elements = []
#
# for element in first_track:
#     elements.append(element)
#
# first_element = elements[0]
# tiny_elements = []
#
# for tiny_el in first_element:
#     tiny_elements.append(tiny_el)

print('hi')