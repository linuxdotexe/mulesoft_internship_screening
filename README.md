# MuleSoft Internship Screening Test Code

The purpose of this document is to explain what I had done in this program.

## Problem Statement

> **Connect to the SQLite database** (or any Database you know): Learn how to download SQLiteJDBC driver and connect to an existing SQLite database using JDBC.
> 
> 
> **Creating a new SQLite database** – Learn how to create a new SQLite database from a Java (any language) program using SQLiteJDBC driver or related driver.
> 
> **Creating a new table (Movies)** using JDBC / Other Languages – before working with data, you need to create a table called Movies. Learn how to create a new table in an SQLite database from a Java (any language) program.
> 
> **Inserting data into Movies table** from a Java (any language) program
> 
> **Querying data from Movies table** with or without parameters – after having the movies data in the table, you need to query the movie details (name, actor, actress, director, year of release) using a SELECT statement. You will need to write a program to issue a simple SELECT statement to query all rows from the Movies table, as well as use a query with parameter like actor name to select movies based on the actor's name.
> 

This is how I satisfied the above mentioned constraints.

## Connecting to and creating an SQLite Database

I have imported the `sqlite3` to start using the SQLite databases. Then, I created an object `conn` which makes the connection to the SQLite database `movie.db`. I did this with the following code

```python
import sqlite3
.
.
conn = sqlite3.connect('movie.db')
```

The following initialization connects the program to the `movie.db` database and in case of the database not existing, it creates a new database under the provided name.

## Creating a new table (Movies)

I have created a new table with the required columns i.e., movie name, lead actor's name, lead actress' name, director's name and the year of release. To do this, I first created a cursor to pass commands to the database and execute them from the program.

```python
c = conn.cursor()
```

Then, I wrote an execute function to create a table with all the required columns

```python
c.execute("""CREATE TABLE movies (
    movie text,
    actor text,
    actress text,
    director text,
    year integer
)""")
```

Here, the triple quotes indicate spanning strings and these are used for readability purposes. If these are not used, we have to write the command as follows which doesn't seem very readable.

```python
c.execute("CREATE TABLE movies ( movie text, actor text, actress text, director text, year integer)")
```

**NOTE**: Even though not the best readability choice, I think using short variables such as `c` and `conn` is  better since we use these objects through out the program multiple times and naming these something more than what we did right now might not be developer friendly.

## Inserting data into Movies table

I have made a list of my favorite movies I decided to include in this new table I have created. Giving all the movies as a single input seemed a simpler option rather than having to write execute commands for each movie, so I made a tuple `movies_list` where I stored the list of movies with the required details.

```python
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
```

I used the `executemany` function in the `sqlite3` library and made use of the `sqlite3` placeholder i.e., `?`.

```python
c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)", movie_list)
```

This inserts all the movies in the list into the table created earlier.

## Querying data from Movies table

I have written one query to fetch all the data in the table and multiple queries to filter the available data.

```python
c.execute("SELECT * FROM movies")
```

The above query selects all the data available in the `movies` table. The below are the more filtered queries

1. Movies with Jake Gyllenhaal as lead actor

```python
c.execute("SELECT * FROM movies WHERE actor = 'Jake Gyllenhaal'")
```

1. Movies directed by Quentin Tarantino in chronological order

```python
c.execute("SELECT * FROM movies WHERE director = 'Quentin Tarantino' ORDER BY year")
```

1. Movies with Jake Gyllenhaal and Rene Russo

```python
c.execute("SELECT * FROM movies WHERE actor = 'Jake Gyllenhaal' AND actress = 'Rene Russo'")
```

1. Movies released before 2000

```python
c.execute("SELECT * FROM movies WHERE year < 2000")
```

1. Movies directed by Quentin Tarantino starring Samuel L. Jackson

```python
c.execute("SELECT * FROM movies WHERE director = 'Quentin Tarantino' AND actor = 'Samuel L. Jackson'")
```

Then, I created a variable `items` and used the `fetchall()` function to get the tuple output of the data into `items`. Now, I used the `tabulate` library to format the output with the following code

```python
print(tabulate(items, headers=['Movie', 'Actor', 'Actress', 'Director', 'Year'], tablefmt='orgtbl'))
```

### NOTE

Many of the query commands are commented out. This is because I have observed that the output of the last written query is being sent to the `fetchall` function and the rest are being over written. I haven't got to see how to overcome this problem so I found commenting unused queries works fine at the moment.

## Recreation of the code

You might want to install the `tabulate` library before running the program. You can do that with this command

```bash
pip3 install tabulate
```

Now, you can run the code. The first output would be the entire `movies` table. Then, as you uncomment each query, you can see the individual outputs.

## Conclusion

This has been a brief explanation about the code I have written for the MuleSoft Internship Screening Test.