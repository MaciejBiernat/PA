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
    

    while choose != 5:
        
        commands = ['Get albums by genre', 'Qunatity of albums in each genre',
        'Get album with biggest value in length field', 'Get last album with earliest release year.', 
        'Get last album with earliest release year in given genre', 'Exit']
        display.print_albums_list(albums)
        display.print_program_menu(commands)
      

        

        choose = int(input("Please provide your choose: "))
        message = commands[choose]
        display.print_command_result(message)
        if message == 'Get albums by genre':
            genre = input("Pleae provide a music genre: ")
            albums_data = music_reports.get_albums_by_genre(albums, genre)
            for album in albums_data:
                display.print_album_info(album)
        if message == 'Qunatity of albums in each genre':
            result = music_reports.get_genre_stats(albums)
            message = str(result)
            display.print_command_result(message)
        if message == 'Get album with biggest value in length field':
            albums_data = music_reports.get_longest_album(albums)
            for album in albums_data:
                display.print_album_info(album)
        else:
            print("dupas")







    
# get_genre_stats(albums)
# get_longest_album(albums)
# get_last_oldest(albums)
# et_last_oldest_of_genre(albums, genre)


if __name__ == '__main__':
    main()
