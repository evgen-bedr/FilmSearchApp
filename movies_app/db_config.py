dbconfig = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'movies'
}

dbconfig_search = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'movies'
}

LIMIT = 10
OFFSET = 0



def query_film_link(film_name):
    query = f"""
        SELECT
    f.film_name,
    COALESCE(f.film_year, '---') AS year,
    COALESCE(f.country, '---') AS country, 
    COALESCE(f.rating, '---') AS rating,
    COALESCE(f.duration, '---') AS duration,
    GROUP_CONCAT(DISTINCT a.actors_name ORDER BY a.actors_name SEPARATOR ', ') AS actors_names,
    GROUP_CONCAT(DISTINCT d.directors_name ORDER BY d.directors_name SEPARATOR ', ') AS directors_names,
    GROUP_CONCAT(DISTINCT g.genres_name ORDER BY g.genres_name SEPARATOR ', ') AS genres,
    downloaded_img
    FROM
        films f
    LEFT JOIN filmsactors fa ON f.id = fa.film_id
    LEFT JOIN actors a ON fa.actor_id = a.id
    LEFT JOIN filmsdirectors fd ON f.id = fd.film_id
    LEFT JOIN directors d ON fd.director_id = d.id
    LEFT JOIN filmsgenres fg ON f.id = fg.film_id
    LEFT JOIN genres g ON fg.genre_id = g.id
    WHERE
        f.film_name = "{film_name}"
    GROUP BY
        f.film_name, f.film_year, f.country, f.rating, f.duration, downloaded_img
    """
    return query

########################################################################
# TOP FILMS BY RATING desc
########################################################################
def query_films_by_rating(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    ORDER BY f.rating DESC
    LIMIT {limit} OFFSET {offset};
    """


########################################################################
# TV SERIES
########################################################################
def query_serials(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name,
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_type = 'serial'
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """


########################################################################
# TOP FILMS
########################################################################
def query_top_rated(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    ORDER BY f.rating DESC
    LIMIT {limit} OFFSET {offset};
    """

def query_lowest_rated(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    ORDER BY f.rating ASC
    LIMIT {limit} OFFSET {offset};
    """

########################################################################
# YEARS
########################################################################

def generate_query_for_year(year, limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = {year}
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_year_2024(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = 2024
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_year_2023(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = 2023
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_year_2022(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = 2022
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_year_2021(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = 2021
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_year_2020(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = 2020
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """
def query_year_2019(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = 2019
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """
def query_year_2018(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = 2018
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_year_2017(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = 2017
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_year_2016(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = 2016
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_year_2015(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = 2015
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_year_2014(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year = 2014
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def generate_query_for_year_others(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_year < 2014
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

########################################################################
# GENRES
########################################################################
def query_comedy(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE g.genres_name = "Комедии"
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img, f.film_year
    ORDER BY f.film_year DESC
    LIMIT {limit} OFFSET {offset};
    """

def query_action(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE g.genres_name = "Боевики"
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img, f.film_year
    ORDER BY f.film_year DESC
    LIMIT {limit} OFFSET {offset};
    """

def query_detective(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE g.genres_name = "Детективы"
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img, f.film_year
    ORDER BY f.film_year DESC
    LIMIT {limit} OFFSET {offset};
    """

def query_drama(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE g.genres_name = "Драмы"
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img, f.film_year
    ORDER BY f.film_year DESC
    LIMIT {limit} OFFSET {offset};
    """

def query_crime(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE g.genres_name = "Криминал"
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img, f.film_year
    ORDER BY f.film_year DESC
    LIMIT {limit} OFFSET {offset};
    """

def query_sports(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE g.genres_name = "Спортивные"
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img, f.film_year
    ORDER BY f.film_year DESC
    LIMIT {limit} OFFSET {offset};
    """

def query_horror(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE g.genres_name = "Ужасы"
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img, f.film_year
    ORDER BY f.film_year DESC
    LIMIT {limit} OFFSET {offset};
    """

def query_fantasy(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE g.genres_name = "Фантастика"
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img, f.film_year
    ORDER BY f.film_year DESC
    LIMIT {limit} OFFSET {offset};
    """

def query_family(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE g.genres_name = "Семейные"
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img, f.film_year
    ORDER BY f.film_year DESC
    LIMIT {limit} OFFSET {offset};
    """

def query_cartoons(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE g.genres_name = "Мультфильмы"
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img, f.film_year
    ORDER BY f.film_year DESC
    LIMIT {limit} OFFSET {offset};
    """

########################################################################
# COUNTRIES
########################################################################

def query_country_usa(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name,
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.country = 'США'
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_country_spain(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name,
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.country = 'Испания'
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_country_japan(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name,
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.country = 'Япония'
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

########################################################################
# ACTORS
########################################################################

def query_actors(limit, offset):
    limit = LIMIT
    return f"""
    SELECT actors_name FROM actors
    LIMIT {limit} OFFSET {offset};
    """

########################################################################
# DIRECTORS
########################################################################

def query_directors(limit, offset):
    limit = LIMIT
    return f"""
    SELECT directors_name FROM directors
    LIMIT {limit} OFFSET {offset};
    """





def query_film_search_user(limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_name LIKE %s
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_film_search_user(search_text, limit, offset):
    limit = LIMIT
    return f"""
    SELECT 
      f.film_name, 
      COALESCE(f.country, '---') AS country, 
      COALESCE(f.rating, '---') AS rating,
      COALESCE(f.duration, '---') AS duration,
      GROUP_CONCAT(g.genres_name SEPARATOR ', ') AS genres,
      downloaded_img
    FROM films f
    LEFT JOIN filmsgenres fg ON fg.film_id = f.id
    LEFT JOIN genres g ON g.id = fg.genre_id
    WHERE f.film_name LIKE %s
    GROUP BY f.film_name, f.country, f.rating, f.duration, downloaded_img
    LIMIT {limit} OFFSET {offset};
    """

def query_actor_search_user(search_text, limit, offset):
    limit = LIMIT
    return f"""
    SELECT actors_name 
    FROM actors 
    WHERE actors_name LIKE %s
    LIMIT {limit} OFFSET {offset};
    """


def query_director_search_user(search_text, limit, offset):
    limit = LIMIT
    return f"""
    SELECT directors_name 
    FROM directors 
    WHERE directors_name LIKE %s
    LIMIT {limit} OFFSET {offset};
    """
