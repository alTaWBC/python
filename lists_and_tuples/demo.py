from nested_data import albums

menu = """Please choose your album (invalid choice exits):"""
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print(menu)
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break
    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):  # type:ignore
        print(f"{index + 1}: {song}")
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):  # type:ignore
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]  # type:ignore
        print(f"Playing {title}")
    print("=" * 40)
