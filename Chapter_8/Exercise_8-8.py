def make_album(artist, title, n_tracks=''):
    album = {'artist': artist, 'title': title}
    return album

while True:
    print("\nPlease enter the artist and the title of a music album: ")
    print("Enter 'q' any time to quit.")
    artist = input("Artist: ")
    if artist == 'q':
        break
    title = input("Title: ")
    if title == 'q':
        break
    new_album = make_album(artist, title)
    print(new_album)

