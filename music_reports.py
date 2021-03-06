

def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    
    
    albums_data = []
    for line in albums:
        if genre in albums:
            albums_data.append(line)       
    return albums_data
            

def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """
    genre_stats = {}
    genre_col = 3
    for line in albums:
        if line[genre_col] not in genre_stats:
            genre_stats[line[genre_col]] = 1
        else: 
            genre_stats[line[genre_col]] += 1
    return genre_stats
    

def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    LENGTH_COL = 4
    max_l = 0
    longest_albums = []
    for line in albums:
        length = to_time(line[LENGTH_COL])
        if length > max_l:
            max_l = length
    for line in albums:
        if to_time(line[LENGTH_COL]) == max_l:
            longest_albums.append(line)
    return longest_albums
    


def get_last_oldest(albums):
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """
    DATE_COL = 2
    earliests_albums = []
    rel_date = map(lambda line: int(line[DATE_COL]), albums)
    min_year = min(rel_date)
    for line in albums:
        if min_year == int(line[DATE_COL]):
            earliests_albums.append(line)
    return earliests_albums


def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """


def to_time(stro):
    """
    converts time in format "minutes:seconds" (string) to seconds (int)
    """
    SEC_IN_MIN = 60
    min_sec = stro.split(':')
    return int(min_sec[0])*SEC_IN_MIN + int(min_sec[1])

def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18             
             231 + 320 seconds = 551 seconds

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    DURATION = 4
    durations = map(lambda album: to_time(album[DURATION]), albums)
    total = sum(durations)
    return int(total / 60) + ((total % 60)/ 60)

 
        