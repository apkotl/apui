from src.databases.dependencies import AsyncSessionDep

from src.orm.books import (
    BookGenresOrm,
    BooksOrm,
    AuthorsOrm,
    ReadingLevel
)


async def insert_bookgenres(session: AsyncSessionDep):
    genre = BookGenresOrm(name="Fantasy")
    session.add(genre)
    genre = BookGenresOrm(name="Historical Fiction")
    session.add(genre)
    genre = BookGenresOrm(name="Adventure")
    session.add(genre)
    genre = BookGenresOrm(name="Poetry")
    session.add(genre)
    genre = BookGenresOrm(name="Mystery")
    session.add(genre)
    genre = BookGenresOrm(name="Science Fiction")
    session.add(genre)
    genre = BookGenresOrm(name="Romance")
    session.add(genre)
    genre = BookGenresOrm(name="Thriller")
    session.add(genre)
    await  session.commit()


async def insert_books(session: AsyncSessionDep):
    await insert_bookgenres(session)

    # Author 0
    author = AuthorsOrm(
        first_name="Cixin",
        last_name="Liu"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-7-536-69293-0",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.Adult,
        title="The Three-Body Problem",
        first_publication_year=2008,
        volume=390
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-1784971595",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.Adult,
        title="The Dark Forest",
        first_publication_year=2008,
        volume=400
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-0765377104",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.Adult,
        title="Death's End",
        first_publication_year=2010,
        volume=592
    )
    session.add(book)
    await session.commit()

    # Author 1 - J.K. Rowling (Harry Potter series)
    author = AuthorsOrm(
        first_name="Joanne",
        last_name="Rowling"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0439708180",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Children,
        title="Harry Potter and the Philosopher's Stone",
        first_publication_year=1997,
        volume=223
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0439064873",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Children,
        title="Harry Potter and the Chamber of Secrets",
        first_publication_year=1998,
        volume=251
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0439136365",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Children,
        title="Harry Potter and the Prisoner of Azkaban",
        first_publication_year=1999,
        volume=317
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0439139601",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.YoungAdult,
        title="Harry Potter and the Goblet of Fire",
        first_publication_year=2000,
        volume=636
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0439358071",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.YoungAdult,
        title="Harry Potter and the Order of the Phoenix",
        first_publication_year=2003,
        volume=766
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0439784542",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.YoungAdult,
        title="Harry Potter and the Half-Blood Prince",
        first_publication_year=2005,
        volume=607
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0545010221",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.YoungAdult,
        title="Harry Potter and the Deathly Hallows",
        first_publication_year=2007,
        volume=607
    )
    session.add(book)

    await session.commit()

    # Author 2 - Walter Scott
    author = AuthorsOrm(
        first_name="Walter",
        last_name="Scott"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0140430738",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="Waverley",
        first_publication_year=1814,
        volume=448
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140436587",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="Ivanhoe",
        first_publication_year=1819,
        volume=512
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140431216",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="Rob Roy",
        first_publication_year=1817,
        volume=464
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140435665",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="The Heart of Midlothian",
        first_publication_year=1818,
        volume=672
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140436600",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="Kenilworth",
        first_publication_year=1821,
        volume=544
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140430752",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="The Bride of Lammermoor",
        first_publication_year=1819,
        volume=352
    )
    session.add(book)

    await session.commit()

    # Author 3 - Alexandre Dumas
    author = AuthorsOrm(
        first_name="Alexandre",
        last_name="Dumas"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0140449266",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="The Three Musketeers",
        first_publication_year=1844,
        volume=625
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140449280",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="Twenty Years After",
        first_publication_year=1845,
        volume=704
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140449303",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="The Vicomte of Bragelonne",
        first_publication_year=1847,
        volume=928
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140449136",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.Adult,
        title="The Count of Monte Cristo",
        first_publication_year=1844,
        volume=1276
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140436297",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="The Queen Margot",
        first_publication_year=1845,
        volume=688
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140437065",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="The Black Tulip",
        first_publication_year=1850,
        volume=256
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140444425",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="The Man in the Iron Mask",
        first_publication_year=1847,
        volume=480
    )
    session.add(book)

    await session.commit()

    # Author 4 - Stephen King
    author = AuthorsOrm(
        first_name="Stephen",
        last_name="King"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0307743657",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="The Shining",
        first_publication_year=1977,
        volume=447
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-1501142970",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="It",
        first_publication_year=1986,
        volume=1138
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-1501156748",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="Carrie",
        first_publication_year=1974,
        volume=199
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-1501144523",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="Pet Sematary",
        first_publication_year=1983,
        volume=374
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-1501143515",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="Salem's Lot",
        first_publication_year=1975,
        volume=439
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-1501182099",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="Misery",
        first_publication_year=1987,
        volume=310
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-1501161216",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="Doctor Sleep",
        first_publication_year=2013,
        volume=531
    )
    session.add(book)

    await session.commit()

    # Author 5 - James Fenimore Cooper
    author = AuthorsOrm(
        first_name="James Fenimore",
        last_name="Cooper"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0140390070",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="The Last of the Mohicans",
        first_publication_year=1826,
        volume=384
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140390049",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="The Deerslayer",
        first_publication_year=1841,
        volume=560
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140390025",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="The Pathfinder",
        first_publication_year=1840,
        volume=512
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140390032",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="The Pioneers",
        first_publication_year=1823,
        volume=464
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140390018",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="The Prairie",
        first_publication_year=1827,
        volume=416
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140435238",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="The Pilot",
        first_publication_year=1824,
        volume=448
    )
    session.add(book)

    await session.commit()

    # Author 6 - Isaac Asimov
    author = AuthorsOrm(
        first_name="Isaac",
        last_name="Asimov"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0553293357",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="Foundation",
        first_publication_year=1951,
        volume=244
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0553293371",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="Foundation and Empire",
        first_publication_year=1952,
        volume=247
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0553293395",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="Second Foundation",
        first_publication_year=1953,
        volume=279
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0553294385",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.YoungAdult,
        title="I, Robot",
        first_publication_year=1950,
        volume=253
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0553565072",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="The Caves of Steel",
        first_publication_year=1954,
        volume=206
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0553294408",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="The Naked Sun",
        first_publication_year=1957,
        volume=224
    )
    session.add(book)

    await session.commit()

    # Author 7 - Arthur C. Clarke
    author = AuthorsOrm(
        first_name="Arthur Charles",
        last_name="Clarke"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0451457998",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="2001: A Space Odyssey",
        first_publication_year=1968,
        volume=297
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0345444059",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="Childhood's End",
        first_publication_year=1953,
        volume=214
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0345452474",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="Rendezvous with Rama",
        first_publication_year=1973,
        volume=243
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0345358059",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="The City and the Stars",
        first_publication_year=1956,
        volume=247
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0345444462",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.YoungAdult,
        title="A Fall of Moondust",
        first_publication_year=1961,
        volume=224
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0345358066",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="Imperial Earth",
        first_publication_year=1975,
        volume=304
    )
    session.add(book)

    await session.commit()

    # Author 8 - Robert A. Heinlein
    author = AuthorsOrm(
        first_name="Robert Anson",
        last_name="Heinlein"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0441788385",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="Stranger in a Strange Land",
        first_publication_year=1961,
        volume=525
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0441783589",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.YoungAdult,
        title="Starship Troopers",
        first_publication_year=1959,
        volume=335
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0441810765",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="Time Enough for Love",
        first_publication_year=1973,
        volume=605
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0441173488",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="The Moon Is a Harsh Mistress",
        first_publication_year=1966,
        volume=382
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0441020836",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.YoungAdult,
        title="Red Planet",
        first_publication_year=1949,
        volume=201
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0441558537",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.YoungAdult,
        title="Have Space Suit—Will Travel",
        first_publication_year=1958,
        volume=224
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0441322084",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="Friday",
        first_publication_year=1982,
        volume=368
    )
    session.add(book)

    await session.commit()

    # Author 9 - Arthur Conan Doyle
    author = AuthorsOrm(
        first_name="Arthur Conan",
        last_name="Doyle"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0140439083",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.YoungAdult,
        title="A Study in Scarlet",
        first_publication_year=1887,
        volume=123
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140439106",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.YoungAdult,
        title="The Sign of Four",
        first_publication_year=1890,
        volume=138
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140350265",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.YoungAdult,
        title="The Adventures of Sherlock Holmes",
        first_publication_year=1892,
        volume=307
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140621006",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.YoungAdult,
        title="The Hound of the Baskervilles",
        first_publication_year=1902,
        volume=256
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140437522",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.YoungAdult,
        title="The Return of Sherlock Holmes",
        first_publication_year=1905,
        volume=378
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140437546",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="The Lost World",
        first_publication_year=1912,
        volume=224
    )
    session.add(book)

    await session.commit()

    # Author 10 - Agatha Christie
    author = AuthorsOrm(
        first_name="Agatha",
        last_name="Christie"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0062073488",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.Adult,
        title="The Murder of Roger Ackroyd",
        first_publication_year=1926,
        volume=288
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0062693662",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.Adult,
        title="Murder on the Orient Express",
        first_publication_year=1934,
        volume=256
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0062073563",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.Adult,
        title="And Then There Were None",
        first_publication_year=1939,
        volume=264
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0062074010",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.Adult,
        title="Death on the Nile",
        first_publication_year=1937,
        volume=352
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0062073471",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.Adult,
        title="The ABC Murders",
        first_publication_year=1936,
        volume=256
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0062073464",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.Adult,
        title="Hercule Poirot's Christmas",
        first_publication_year=1938,
        volume=288
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0062073549",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.Adult,
        title="The Body in the Library",
        first_publication_year=1942,
        volume=224
    )
    session.add(book)

    await session.commit()

    # Author 11 - Alexander Pushkin
    author = AuthorsOrm(
        first_name="Alexander",
        last_name="Pushkin"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0140448108",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="Eugene Onegin",
        first_publication_year=1833,
        volume=240
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140440430",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.YoungAdult,
        title="Ruslan and Lyudmila",
        first_publication_year=1820,
        volume=96
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140446852",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="The Bronze Horseman and Other Poems",
        first_publication_year=1837,
        volume=128
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140445831",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="Selected Lyric Poetry",
        first_publication_year=1825,
        volume=192
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140447071",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.YoungAdult,
        title="The Tale of Tsar Saltan",
        first_publication_year=1831,
        volume=64
    )
    session.add(book)

    await session.commit()

    # Author 12 - William Shakespeare
    author = AuthorsOrm(
        first_name="William",
        last_name="Shakespeare"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0140714548",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="Shakespeare's Sonnets",
        first_publication_year=1609,
        volume=128
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140424850",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="Venus and Adonis",
        first_publication_year=1593,
        volume=80
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140424867",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="The Rape of Lucrece",
        first_publication_year=1594,
        volume=96
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140714555",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="A Lover's Complaint",
        first_publication_year=1609,
        volume=48
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140714562",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.AllAges,
        title="The Phoenix and the Turtle",
        first_publication_year=1601,
        volume=32
    )
    session.add(book)

    await session.commit()

    # Author 13 - Lord Byron
    author = AuthorsOrm(
        first_name="George Gordon",
        last_name="Byron"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0140422887",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="Childe Harold's Pilgrimage",
        first_publication_year=1812,
        volume=224
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140422894",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="Don Juan",
        first_publication_year=1819,
        volume=672
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140422900",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="The Corsair",
        first_publication_year=1814,
        volume=96
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140422917",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="She Walks in Beauty and Other Poems",
        first_publication_year=1815,
        volume=128
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140422924",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.YoungAdult,
        title="The Prisoner of Chillon",
        first_publication_year=1816,
        volume=64
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0140422931",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="Manfred",
        first_publication_year=1817,
        volume=88
    )
    session.add(book)

    await session.commit()

    # Author 14 - Margaret Mitchell
    author = AuthorsOrm(
        first_name="Margaret",
        last_name="Mitchell"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-1416548942",
        author_id=author.id,
        genre_id=7,  # Romance
        reading_level=ReadingLevel.Adult,
        title="Gone with the Wind",
        first_publication_year=1936,
        volume=1037
    )
    session.add(book)

    await session.commit()

    # Author 15 - Jane Austen
    author = AuthorsOrm(
        first_name="Jane",
        last_name="Austen"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0141439518",
        author_id=author.id,
        genre_id=7,  # Romance
        reading_level=ReadingLevel.YoungAdult,
        title="Pride and Prejudice",
        first_publication_year=1813,
        volume=432
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0141439662",
        author_id=author.id,
        genre_id=7,  # Romance
        reading_level=ReadingLevel.YoungAdult,
        title="Sense and Sensibility",
        first_publication_year=1811,
        volume=409
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0141439587",
        author_id=author.id,
        genre_id=7,  # Romance
        reading_level=ReadingLevel.YoungAdult,
        title="Emma",
        first_publication_year=1815,
        volume=474
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0141439679",
        author_id=author.id,
        genre_id=7,  # Romance
        reading_level=ReadingLevel.YoungAdult,
        title="Mansfield Park",
        first_publication_year=1814,
        volume=560
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0141439686",
        author_id=author.id,
        genre_id=7,  # Romance
        reading_level=ReadingLevel.YoungAdult,
        title="Northanger Abbey",
        first_publication_year=1817,
        volume=272
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0141439693",
        author_id=author.id,
        genre_id=7,  # Romance
        reading_level=ReadingLevel.Adult,
        title="Persuasion",
        first_publication_year=1817,
        volume=249
    )
    session.add(book)

    await session.commit()

    # Author 16 - Clifford D. Simak
    author = AuthorsOrm(
        first_name="Clifford Donald",
        last_name="Simak"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0020254409",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="City",
        first_publication_year=1952,
        volume=251
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0020254416",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="Way Station",
        first_publication_year=1963,
        volume=210
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0020254423",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="Time and Again",
        first_publication_year=1951,
        volume=188
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0020254430",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="All Flesh Is Grass",
        first_publication_year=1965,
        volume=192
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0020254447",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.YoungAdult,
        title="The Goblin Reservation",
        first_publication_year=1968,
        volume=216
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0020254454",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.Adult,
        title="A Choice of Gods",
        first_publication_year=1972,
        volume=201
    )
    session.add(book)

    await session.commit()

    # Author 17 - Edgar Allan Poe
    author = AuthorsOrm(
        first_name="Edgar Allan",
        last_name="Poe"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0486266855",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.YoungAdult,
        title="Tales of Mystery and Imagination",
        first_publication_year=1845,
        volume=272
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486454061",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="The Fall of the House of Usher and Other Tales",
        first_publication_year=1839,
        volume=128
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486266862",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.YoungAdult,
        title="The Murders in the Rue Morgue",
        first_publication_year=1841,
        volume=64
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486454078",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="The Raven and Other Poems",
        first_publication_year=1845,
        volume=96
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486266879",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="The Pit and the Pendulum and Other Stories",
        first_publication_year=1842,
        volume=112
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486454085",
        author_id=author.id,
        genre_id=5,  # Mystery
        reading_level=ReadingLevel.YoungAdult,
        title="The Gold Bug and Other Stories",
        first_publication_year=1843,
        volume=128
    )
    session.add(book)

    await session.commit()

    # Author 18 - J.R.R. Tolkien
    author = AuthorsOrm(
        first_name="John Ronald Reuel",
        last_name="Tolkien"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0547928227",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.AllAges,
        title="The Hobbit",
        first_publication_year=1937,
        volume=366
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0544003415",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.YoungAdult,
        title="The Fellowship of the Ring",
        first_publication_year=1954,
        volume=423
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0544003422",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.YoungAdult,
        title="The Two Towers",
        first_publication_year=1954,
        volume=352
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0544003439",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.YoungAdult,
        title="The Return of the King",
        first_publication_year=1955,
        volume=416
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0544338012",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="The Silmarillion",
        first_publication_year=1977,
        volume=365
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0544337992",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="Unfinished Tales",
        first_publication_year=1980,
        volume=472
    )
    session.add(book)

    await session.commit()

    # Author 19 - George R.R. Martin
    author = AuthorsOrm(
        first_name="George Raymond Richard",
        last_name="Martin"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0553103540",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="A Game of Thrones",
        first_publication_year=1996,
        volume=694
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0553108033",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="A Clash of Kings",
        first_publication_year=1998,
        volume=761
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0553106633",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="A Storm of Swords",
        first_publication_year=2000,
        volume=973
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0553106647",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="A Feast for Crows",
        first_publication_year=2005,
        volume=753
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0553106664",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="A Dance with Dragons",
        first_publication_year=2011,
        volume=1016
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-1524796280",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="Fire & Blood",
        first_publication_year=2018,
        volume=736
    )
    session.add(book)

    await session.commit()

    # Author 20 - Dan Brown
    author = AuthorsOrm(
        first_name="Dan",
        last_name="Brown"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0307474278",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="The Da Vinci Code",
        first_publication_year=2003,
        volume=454
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0743493468",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="Angels & Demons",
        first_publication_year=2000,
        volume=713
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0307950680",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="The Lost Symbol",
        first_publication_year=2009,
        volume=671
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0385537858",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="Inferno",
        first_publication_year=2013,
        volume=480
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0385514231",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="Digital Fortress",
        first_publication_year=1998,
        volume=510
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-1400079179",
        author_id=author.id,
        genre_id=8,  # Thriller
        reading_level=ReadingLevel.Adult,
        title="Origin",
        first_publication_year=2017,
        volume=480
    )
    session.add(book)

    await session.commit()

    # Author 21 - Ernest Hemingway
    author = AuthorsOrm(
        first_name="Ernest",
        last_name="Hemingway"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0684801223",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="The Old Man and the Sea",
        first_publication_year=1952,
        volume=127
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0684837888",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="A Farewell to Arms",
        first_publication_year=1929,
        volume=355
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0684803357",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="For Whom the Bell Tolls",
        first_publication_year=1940,
        volume=471
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0684800714",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="The Sun Also Rises",
        first_publication_year=1926,
        volume=251
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0684837895",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="A Moveable Feast",
        first_publication_year=1964,
        volume=211
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0684804453",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="Islands in the Stream",
        first_publication_year=1970,
        volume=466
    )
    session.add(book)

    await session.commit()

    # Author 22 - Mark Twain
    author = AuthorsOrm(
        first_name="Samuel Langhorne",
        last_name="Clemens"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0486400778",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.Children,
        title="The Adventures of Tom Sawyer",
        first_publication_year=1876,
        volume=274
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486280615",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="Adventures of Huckleberry Finn",
        first_publication_year=1884,
        volume=366
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486415864",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.Children,
        title="The Prince and the Pauper",
        first_publication_year=1881,
        volume=234
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486415871",
        author_id=author.id,
        genre_id=6,  # Science Fiction
        reading_level=ReadingLevel.YoungAdult,
        title="A Connecticut Yankee in King Arthur's Court",
        first_publication_year=1889,
        volume=301
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486266909",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.YoungAdult,
        title="Pudd'nhead Wilson",
        first_publication_year=1894,
        volume=216
    )
    session.add(book)

    await session.commit()

    # Author 23 - Oscar Wilde
    author = AuthorsOrm(
        first_name="Oscar",
        last_name="Wilde"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0141439570",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="The Picture of Dorian Gray",
        first_publication_year=1890,
        volume=254
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486270777",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.Children,
        title="The Happy Prince and Other Tales",
        first_publication_year=1888,
        volume=96
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486266985",
        author_id=author.id,
        genre_id=3,  # Adventure
        reading_level=ReadingLevel.Children,
        title="A House of Pomegranates",
        first_publication_year=1891,
        volume=128
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486266992",
        author_id=author.id,
        genre_id=4,  # Poetry
        reading_level=ReadingLevel.Adult,
        title="The Ballad of Reading Gaol",
        first_publication_year=1898,
        volume=48
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0486415888",
        author_id=author.id,
        genre_id=7,  # Romance
        reading_level=ReadingLevel.Adult,
        title="De Profundis",
        first_publication_year=1905,
        volume=160
    )
    session.add(book)

    await session.commit()

    # Author 24 - Charles Dickens
    author = AuthorsOrm(
        first_name="Charles",
        last_name="Dickens"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0141439747",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.YoungAdult,
        title="Oliver Twist",
        first_publication_year=1838,
        volume=608
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0141439273",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="David Copperfield",
        first_publication_year=1850,
        volume=882
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0141439600",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.YoungAdult,
        title="Great Expectations",
        first_publication_year=1861,
        volume=544
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0141439280",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.AllAges,
        title="A Christmas Carol",
        first_publication_year=1843,
        volume=104
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0141439631",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="A Tale of Two Cities",
        first_publication_year=1859,
        volume=489
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0141439297",
        author_id=author.id,
        genre_id=2,  # Historical Fiction
        reading_level=ReadingLevel.Adult,
        title="Hard Times",
        first_publication_year=1854,
        volume=368
    )
    session.add(book)

    await session.commit()

    # Author 25 - Haruki Murakami
    author = AuthorsOrm(
        first_name="Haruki",
        last_name="Murakami"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0375704024",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="Norwegian Wood",
        first_publication_year=1987,
        volume=296
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0375713507",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="Kafka on the Shore",
        first_publication_year=2002,
        volume=436
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0679743460",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="Hard-Boiled Wonderland and the End of the World",
        first_publication_year=1985,
        volume=400
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0375718946",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="The Wind-Up Bird Chronicle",
        first_publication_year=1994,
        volume=607
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0307593313",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="1Q84",
        first_publication_year=2009,
        volume=925
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0385352109",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="Colorless Tsukuru Tazaki and His Years of Pilgrimage",
        first_publication_year=2013,
        volume=298
    )
    session.add(book)

    await session.commit()

    # Author 26 - Paulo Coelho
    author = AuthorsOrm(
        first_name="Paulo",
        last_name="Coelho"
    )
    session.add(author)
    await session.flush()

    book = BooksOrm(
        isbn="978-0061122415",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.YoungAdult,
        title="The Alchemist",
        first_publication_year=1988,
        volume=163
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0061122439",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="The Pilgrimage",
        first_publication_year=1987,
        volume=256
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0061166839",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="Brida",
        first_publication_year=1990,
        volume=208
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0061122446",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="The Valkyries",
        first_publication_year=1992,
        volume=243
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0061343247",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.Adult,
        title="Veronika Decides to Die",
        first_publication_year=1998,
        volume=210
    )
    session.add(book)

    book = BooksOrm(
        isbn="978-0061209420",
        author_id=author.id,
        genre_id=1,  # Fantasy
        reading_level=ReadingLevel.YoungAdult,
        title="The Witch of Portobello",
        first_publication_year=2006,
        volume=288
    )
    session.add(book)

    await session.commit()






"""
async def insert_books_old(session: AsyncSessionDep):
    await insert_bookgenres(session)

    # Author 0
    author = AuthorsOrm(
        first_name="Cixin",
        last_name="Liu"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-7-536-69293-0",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.Adult,
        title="The Three-Body Problem",
        first_publication_year=2008,
        volume=390
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-1784971595",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.Adult,
        title="The Dark Forest",
        first_publication_year=2008,
        volume=400
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-0765377104",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.Adult,
        title="Death's End",
        first_publication_year=2010,
        volume=592
    )
    session.add(book)
    await session.commit()

    # Author 1
    author = AuthorsOrm(
        first_name="Amara",
        last_name="Vance"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-1234567890",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.Adult,
        title="The Crystal Veil",
        first_publication_year=2015,
        volume=320
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-1234567891",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.Adult,
        title="Shadow of the Flame",
        first_publication_year=2017,
        volume=350
    )
    session.add(book)
    await session.commit()

    # Author 2
    author = AuthorsOrm(
        first_name="Jasper",
        last_name="Holt"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-2345678901",
        author_id=author.id,
        genre_id=2,
        reading_level=ReadingLevel.Adult,
        title="The Last Crown",
        first_publication_year=2010,
        volume=400
    )
    session.add(book)
    await session.commit()

    # Author 3
    author = AuthorsOrm(
        first_name="Lila",
        last_name="Marwood"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-3456789012",
        author_id=author.id,
        genre_id=3,
        reading_level=ReadingLevel.YoungAdult,
        title="Treasure of the Deep",
        first_publication_year=2018,
        volume=280
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-3456789013",
        author_id=author.id,
        genre_id=3,
        reading_level=ReadingLevel.YoungAdult,
        title="Skyward Journey",
        first_publication_year=2020,
        volume=300
    )
    session.add(book)
    await session.commit()

    # Author 4
    author = AuthorsOrm(
        first_name="Elias",
        last_name="Frost"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-4567890123",
        author_id=author.id,
        genre_id=4,
        reading_level=ReadingLevel.AllAges,
        title="Whispers of Dawn",
        first_publication_year=2012,
        volume=150
    )
    session.add(book)
    await session.commit()

    # Author 5
    author = AuthorsOrm(
        first_name="Sofia",
        last_name="Reyes"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-5678901234",
        author_id=author.id,
        genre_id=5,
        reading_level=ReadingLevel.Adult,
        title="The Silent Clue",
        first_publication_year=2019,
        volume=340
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-5678901235",
        author_id=author.id,
        genre_id=5,
        reading_level=ReadingLevel.Adult,
        title="Enigma's Shadow",
        first_publication_year=2021,
        volume=360
    )
    session.add(book)
    await session.commit()

    # Author 6
    author = AuthorsOrm(
        first_name="Theo",
        last_name="Grayson"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-6789012345",
        author_id=author.id,
        genre_id=6,
        reading_level=ReadingLevel.Adult,
        title="Starborn Legacy",
        first_publication_year=2014,
        volume=420
    )
    session.add(book)
    await session.commit()

    # Author 7
    author = AuthorsOrm(
        first_name="Nora",
        last_name="Elliot"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-7890123456",
        author_id=author.id,
        genre_id=7,
        reading_level=ReadingLevel.Adult,
        title="Hearts in Time",
        first_publication_year=2016,
        volume=290
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-7890123457",
        author_id=author.id,
        genre_id=7,
        reading_level=ReadingLevel.Adult,
        title="Forever's Promise",
        first_publication_year=2018,
        volume=310
    )
    session.add(book)
    await session.commit()

    # Author 8
    author = AuthorsOrm(
        first_name="Finn",
        last_name="Carver"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-8901234567",
        author_id=author.id,
        genre_id=8,
        reading_level=ReadingLevel.Adult,
        title="Edge of Fear",
        first_publication_year=2020,
        volume=370
    )
    session.add(book)
    await session.commit()

    # Author 9
    author = AuthorsOrm(
        first_name="Isla",
        last_name="Morrow"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-9012345678",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.YoungAdult,
        title="Moonlit Quest",
        first_publication_year=2017,
        volume=330
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-9012345679",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.YoungAdult,
        title="Star of the Realm",
        first_publication_year=2019,
        volume=350
    )
    session.add(book)
    await session.commit()

    # Author 10
    author = AuthorsOrm(
        first_name="Declan",
        last_name="Shaw"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-0123456789",
        author_id=author.id,
        genre_id=2,
        reading_level=ReadingLevel.Adult,
        title="Echoes of Empire",
        first_publication_year=2013,
        volume=380
    )
    session.add(book)
    await session.commit()

    # Author 11
    author = AuthorsOrm(
        first_name="Clara",
        last_name="Wren"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-1234567892",
        author_id=author.id,
        genre_id=3,
        reading_level=ReadingLevel.Children,
        title="Island Adventure",
        first_publication_year=2015,
        volume=200
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-1234567893",
        author_id=author.id,
        genre_id=3,
        reading_level=ReadingLevel.Children,
        title="Pirate's Quest",
        first_publication_year=2017,
        volume=220
    )
    session.add(book)
    await session.commit()

    # Author 12
    author = AuthorsOrm(
        first_name="Miles",
        last_name="Sterling"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-2345678902",
        author_id=author.id,
        genre_id=4,
        reading_level=ReadingLevel.AllAges,
        title="Silent Verses",
        first_publication_year=2011,
        volume=140
    )
    session.add(book)
    await session.commit()

    # Author 13
    author = AuthorsOrm(
        first_name="Evie",
        last_name="Haven"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-3456789014",
        author_id=author.id,
        genre_id=5,
        reading_level=ReadingLevel.Adult,
        title="The Hidden Truth",
        first_publication_year=2022,
        volume=390
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-3456789015",
        author_id=author.id,
        genre_id=5,
        reading_level=ReadingLevel.Adult,
        title="Mystery of the Manor",
        first_publication_year=2023,
        volume=410
    )
    session.add(book)
    await session.commit()

    # Author 14
    author = AuthorsOrm(
        first_name="Gideon",
        last_name="Blake"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-4567890124",
        author_id=author.id,
        genre_id=6,
        reading_level=ReadingLevel.Adult,
        title="Quantum Horizon",
        first_publication_year=2016,
        volume=450
    )
    session.add(book)
    await session.commit()

    # Author 15
    author = AuthorsOrm(
        first_name="Aria",
        last_name="Lund"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-5678901236",
        author_id=author.id,
        genre_id=7,
        reading_level=ReadingLevel.YoungAdult,
        title="Love's Last Song",
        first_publication_year=2019,
        volume=270
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-5678901237",
        author_id=author.id,
        genre_id=7,
        reading_level=ReadingLevel.YoungAdult,
        title="Eternal Flame",
        first_publication_year=2021,
        volume=290
    )
    session.add(book)
    await session.commit()

    # Author 16
    author = AuthorsOrm(
        first_name="Silas",
        last_name="Drake"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-6789012346",
        author_id=author.id,
        genre_id=8,
        reading_level=ReadingLevel.Adult,
        title="Dark Pursuit",
        first_publication_year=2018,
        volume=360
    )
    session.add(book)
    await session.commit()

    # Author 17
    author = AuthorsOrm(
        first_name="Maeve",
        last_name="Cullen"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-7890123458",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.Adult,
        title="The Forgotten Realm",
        first_publication_year=2014,
        volume=340
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-7890123459",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.Adult,
        title="Sword of Destiny",
        first_publication_year=2016,
        volume=360
    )
    session.add(book)
    await session.commit()

    # Author 18
    author = AuthorsOrm(
        first_name="Rowan",
        last_name="Fletcher"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-8901234568",
        author_id=author.id,
        genre_id=2,
        reading_level=ReadingLevel.Adult,
        title="The Fallen Kingdom",
        first_publication_year=2012,
        volume=420
    )
    session.add(book)
    await session.commit()

    # Author 19
    author = AuthorsOrm(
        first_name="Lyra",
        last_name="Sage"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-9012345670",
        author_id=author.id,
        genre_id=3,
        reading_level=ReadingLevel.YoungAdult,
        title="Voyage of the Stars",
        first_publication_year=2020,
        volume=310
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-9012345671",
        author_id=author.id,
        genre_id=3,
        reading_level=ReadingLevel.YoungAdult,
        title="The Lost Explorer",
        first_publication_year=2022,
        volume=330
    )
    session.add(book)
    await session.commit()

    # Author 20
    author = AuthorsOrm(
        first_name="Caleb",
        last_name="Vaughn"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-0123456780",
        author_id=author.id,
        genre_id=4,
        reading_level=ReadingLevel.AllAges,
        title="Echoes in Verse",
        first_publication_year=2010,
        volume=160
    )
    session.add(book)
    await session.commit()

    # Author 21
    author = AuthorsOrm(
        first_name="Elise",
        last_name="Barrett"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-1234567894",
        author_id=author.id,
        genre_id=5,
        reading_level=ReadingLevel.Adult,
        title="The Final Secret",
        first_publication_year=2017,
        volume=380
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-1234567895",
        author_id=author.id,
        genre_id=5,
        reading_level=ReadingLevel.Adult,
        title="Shadows of Doubt",
        first_publication_year=2019,
        volume=400
    )
    session.add(book)
    await session.commit()

    # Author 22
    author = AuthorsOrm(
        first_name="Tristan",
        last_name="Kane"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-2345678903",
        author_id=author.id,
        genre_id=6,
        reading_level=ReadingLevel.Adult,
        title="Galactic Dawn",
        first_publication_year=2015,
        volume=430
    )
    session.add(book)
    await session.commit()

    # Author 23
    author = AuthorsOrm(
        first_name="Juna",
        last_name="Asher"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-3456789016",
        author_id=author.id,
        genre_id=7,
        reading_level=ReadingLevel.Adult,
        title="Whispers of Love",
        first_publication_year=2018,
        volume=300
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-3456789017",
        author_id=author.id,
        genre_id=7,
        reading_level=ReadingLevel.Adult,
        title="Fate's Embrace",
        first_publication_year=2020,
        volume=320
    )
    session.add(book)
    await session.commit()

    # Author 24
    author = AuthorsOrm(
        first_name="Felix",
        last_name="Rourke"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-4567890125",
        author_id=author.id,
        genre_id=8,
        reading_level=ReadingLevel.Adult,
        title="The Last Stand",
        first_publication_year=2021,
        volume=350
    )
    session.add(book)
    await session.commit()

    # Author 25
    author = AuthorsOrm(
        first_name="Zara",
        last_name="Whitlock"
    )
    session.add(author)
    await session.flush()
    book = BooksOrm(
        isbn="978-5678901238",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.YoungAdult,
        title="The Eternal Spark",
        first_publication_year=2016,
        volume=340
    )
    session.add(book)
    book = BooksOrm(
        isbn="978-5678901239",
        author_id=author.id,
        genre_id=1,
        reading_level=ReadingLevel.YoungAdult,
        title="Light of the Abyss",
        first_publication_year=2018,
        volume=360
    )
    session.add(book)
    await session.commit()
"""