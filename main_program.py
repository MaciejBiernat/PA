"""
The main program should use functions from music_reports and display modules
"""
import file_handling
import music_reports
import display
filename = 'albums_data.txt'
albums = file_handling.import_data(filename)

def delete_album_by_artist_and_album_name(albums, artist, album_name):
    """
    Deletes album of given name by given artist from list and updates data file

    :param list albums: currently existing albums
    :param str artist: artist who recorded the album
    :param str album_name: name of album to be deleted

    :returns: updated albums' list
    :rtype: list
    """


def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    choose = None
    while choose !=0:
        print("""Welcome to music library. Please choose your function
        1) Get albums by genre
        2) Qunatity of albms in each genre
        3) Get album with biggest value in length field.
        4) Get last album with earliest release year.
        5) Get last album with earliest release year in given genre
        0) Exit
        :
        """)
        choose = input()
        if choose == '1':
            genre = input("Pleae provide a music genre: ")
            music_reports.get_albums_by_genre(albums, genre)
        if choose == '2':
            music_reports.get_genre_stats(albums)


            



    
# get_genre_stats(albums)
# get_longest_album(albums)
# get_last_oldest(albums)
# et_last_oldest_of_genre(albums, genre)


if __name__ == '__main__':
    main()
