def make_album(artist, title, n_tracks=''):
    album = {'artist': artist, 'title': title}
    if n_tracks:
        album['tracks'] = n_tracks
    return album

album1 = make_album('medvedenka', 'my life', 18)
print(album1)
album2 = make_album('mishutka', 'my love')
print(album2)
album3 = make_album('belyash', 'i like ice')
print(album3)