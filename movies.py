import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('movie.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS movies (
    movie text,
    actor text,
    actress text,
    director text,
    year integer,
    UNIQUE (movie, actor, actress, director, year)
)""")

movie_list = [
    ('Enemy', 'Jake Gyllenhaal', 'Mélanie Laurent', 'Denis Villeneuve', 2013),
    ('The Shawshank Redemption', 'Tim Robbins', 'Rita Hayworth', 'Frank Darabont', 1994),
    ('Fight Club', 'Edward Norton', 'Helena Bonham Carter', 'David Fincher', 1999),
    ('SE7EN', 'Brad Pitt', 'Gweneth Paltrow', 'David Fincher', 1995),
    ('Zodiac', 'Robert Downey Jr.', 'Chloe Sevigny', 'David Fincher', 2007),
    ('The Social Network', 'Jesse Eisenberg', 'Rooney Mara', 'David Fincher', 2010),
    ('Gone Girl', 'Ben Affleck', 'Rosamund Pike', 'David Fincher', 2014),
    ('Prisoners', 'Hugh Jackman', 'Viola Davis', 'Denis Villeneuve', 2013),
    ('Donnie Darko', 'Jake Gyllenhaal', 'Jena Malone', 'Richard Kelly', 2001),
    ('Nightcrawler', 'Jake Gyllenhaal', 'Rene Russo', 'Dan Gilroy', 2014),
    ('Demolition', 'Jake Gyllenhaal', 'Naomi Watts', 'Jean-Marc Vallee', 2015),
    ('Velvet Buzzsaw', 'Jake Gyllenhaal', 'Rene Russo', 'Dan Gilroy', 2019),
    ('Pulp Fiction', 'Samuel L. Jackson', 'Uma Thurman', 'Quentin Tarantino', 1994),
    ('Jackie Brown', 'Samuel L. Jackson', 'Pam Grier', 'Quentin Tarantino', 1997),
    ('Django Unchained', 'Jamie Foxx', 'Kerry Washington', 'Quentin Tarantino', 2012),
    ('Inglorious Bastards', 'Brad Pitt', 'Diane Kruger', 'Quentin Tarantino', 2009),
    ('The Hateful Eight', 'Samuel L. Jackson', 'Jennifer Jason Leigh', 'Quentin Tarantino', 2015),
    ('American Gangster', 'Denzel Washington', 'Lymari Nadal', 'Ridley Scott', 2007),
    ('The Firm', 'Tom Cruise', 'Jeanne Tripplehorn', 'Sydney Pollack', 1993),
    ('Devils Advocate', 'Keanu Reaves', 'Charlize Theron', 'Taylor Hackford', 1997),
]
try:
    c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)", movie_list)
except(sqlite3.IntegrityError):
    pass

c.execute("SELECT * FROM movies")

# Movies with Jake Gyllenhaal as lead actor
# c.execute("SELECT * FROM movies WHERE actor = 'Jake Gyllenhaal'")

# Movies directed by Quentin Tarantino in chronological order
# c.execute("SELECT * FROM movies WHERE director = 'Quentin Tarantino' ORDER BY year")

#Movies with Jake Gyllenhaal and Rene Russo
# c.execute("SELECT * FROM movies WHERE actor = 'Jake Gyllenhaal' AND actress = 'Rene Russo'")

# Movies released before 2000
# c.execute("SELECT * FROM movies WHERE year < 2000")

# Movies directed by Quentin Tarantino starring Samuel L. Jackson
# c.execute("SELECT * FROM movies WHERE director = 'Quentin Tarantino' AND actor = 'Samuel L. Jackson'")

items = c.fetchall()
print(tabulate(items, headers=['Movie', 'Actor', 'Actress', 'Director', 'Year'], tablefmt='orgtbl'))

conn.commit()
conn.close()
