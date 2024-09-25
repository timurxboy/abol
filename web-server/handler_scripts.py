import os

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.main.models import Book
from datetime import datetime

books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "Moby Dick", "author": "Herman Melville", "year": 1851},
    {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "Ulysses", "author": "James Joyce", "year": 1922},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
    {"title": "Anna Karenina", "author": "Leo Tolstoy", "year": 1877},
    {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "year": 1880},
    {"title": "Madame Bovary", "author": "Gustave Flaubert", "year": 1857},
    {"title": "The Divine Comedy", "author": "Dante Alighieri", "year": 1320},
    {"title": "Don Quixote", "author": "Miguel de Cervantes", "year": 1605},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez", "year": 1967},
    {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "year": 1890},
    {"title": "Frankenstein", "author": "Mary Shelley", "year": 1818},
    {"title": "The Sound and the Fury", "author": "William Faulkner", "year": 1929},
    {"title": "Wuthering Heights", "author": "Emily Brontë", "year": 1847},
    {"title": "Great Expectations", "author": "Charles Dickens", "year": 1861},
    {"title": "The Grapes of Wrath", "author": "John Steinbeck", "year": 1939},
    {"title": "Lolita", "author": "Vladimir Nabokov", "year": 1955},
    {"title": "Catch-22", "author": "Joseph Heller", "year": 1961},
    {"title": "Beloved", "author": "Toni Morrison", "year": 1987},
    {"title": "The Count of Monte Cristo", "author": "Alexandre Dumas", "year": 1844},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "year": 1847},
    {"title": "Dracula", "author": "Bram Stoker", "year": 1897},
    {"title": "The Old Man and the Sea", "author": "Ernest Hemingway", "year": 1952},
    {"title": "The Metamorphosis", "author": "Franz Kafka", "year": 1915},
    {"title": "Les Misérables", "author": "Victor Hugo", "year": 1862},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953},
    {"title": "Heart of Darkness", "author": "Joseph Conrad", "year": 1899},
    {"title": "The Sun Also Rises", "author": "Ernest Hemingway", "year": 1926},
    {"title": "A Tale of Two Cities", "author": "Charles Dickens", "year": 1859},
    {"title": "Slaughterhouse-Five", "author": "Kurt Vonnegut", "year": 1969},
    {"title": "The Stranger", "author": "Albert Camus", "year": 1942},
    {"title": "Gone with the Wind", "author": "Margaret Mitchell", "year": 1936},
    {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988},
    {"title": "The Shining", "author": "Stephen King", "year": 1977},
    {"title": "Rebecca", "author": "Daphne du Maurier", "year": 1938},
    {"title": "The Bell Jar", "author": "Sylvia Plath", "year": 1963},
    {"title": "The Road", "author": "Cormac McCarthy", "year": 2006},
    {"title": "Of Mice and Men", "author": "John Steinbeck", "year": 1937},
    {"title": "The Scarlet Letter", "author": "Nathaniel Hawthorne", "year": 1850},
    {"title": "Middlemarch", "author": "George Eliot", "year": 1871},
    {"title": "The Trial", "author": "Franz Kafka", "year": 1925},
    {"title": "A Clockwork Orange", "author": "Anthony Burgess", "year": 1962},
    {"title": "On the Road", "author": "Jack Kerouac", "year": 1957},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
    {"title": "East of Eden", "author": "John Steinbeck", "year": 1952},
    {"title": "Invisible Man", "author": "Ralph Ellison", "year": 1952},
    {"title": "Dune", "author": "Frank Herbert", "year": 1965},
    {"title": "The Kite Runner", "author": "Khaled Hosseini", "year": 2003},
    {"title": "Life of Pi", "author": "Yann Martel", "year": 2001},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"title": "The Hunger Games", "author": "Suzanne Collins", "year": 2008},
    {"title": "The Giver", "author": "Lois Lowry", "year": 1993},
    {"title": "The Book Thief", "author": "Markus Zusak", "year": 2005},
    {"title": "The Secret Garden", "author": "Frances Hodgson Burnett", "year": 1911},
    {"title": "Charlotte's Web", "author": "E.B. White", "year": 1952},
    {"title": "A Wrinkle in Time", "author": "Madeleine L'Engle", "year": 1962},
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"title": "The Little Prince", "author": "Antoine de Saint-Exupéry", "year": 1943},
    {"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "year": 1865},
    {"title": "The Wind in the Willows", "author": "Kenneth Grahame", "year": 1908},
    {"title": "The Adventures of Huckleberry Finn", "author": "Mark Twain", "year": 1884},
    {"title": "The Call of the Wild", "author": "Jack London", "year": 1903},
    {"title": "Treasure Island", "author": "Robert Louis Stevenson", "year": 1883},
    {"title": "Peter Pan", "author": "J.M. Barrie", "year": 1904},
    {"title": "The Lion, the Witch and the Wardrobe", "author": "C.S. Lewis", "year": 1950},
    {"title": "The Jungle Book", "author": "Rudyard Kipling", "year": 1894},
    {"title": "Black Beauty", "author": "Anna Sewell", "year": 1877},
    {"title": "Anne of Green Gables", "author": "Lucy Maud Montgomery", "year": 1908},
    {"title": "The Phantom of the Opera", "author": "Gaston Leroux", "year": 1910},
    {"title": "The Hunchback of Notre-Dame", "author": "Victor Hugo", "year": 1831},
    {"title": "The Time Machine", "author": "H.G. Wells", "year": 1895},
    {"title": "The War of the Worlds", "author": "H.G. Wells", "year": 1898},
    {"title": "Dr. Jekyll and Mr. Hyde", "author": "Robert Louis Stevenson", "year": 1886},
    {"title": "The Invisible Man", "author": "H.G. Wells", "year": 1897},
    {"title": "The Strange Case of Dr. Jekyll and Mr. Hyde", "author": "Robert Louis Stevenson", "year": 1886},
    {"title": "The Wonderful Wizard of Oz", "author": "L. Frank Baum", "year": 1900},
    {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "year": 1890},
    {"title": "The Adventures of Tom Sawyer", "author": "Mark Twain", "year": 1876},
    {"title": "Robinson Crusoe", "author": "Daniel Defoe", "year": 1719},
    {"title": "Gulliver's Travels", "author": "Jonathan Swift", "year": 1726},
    {"title": "The Three Musketeers", "author": "Alexandre Dumas", "year": 1844},
    {"title": "Around the World in Eighty Days", "author": "Jules Verne", "year": 1873},
    {"title": "Twenty Thousand Leagues Under the Sea", "author": "Jules Verne", "year": 1870},
]

for book in books:
    Book.objects.create(
        name=book['title'],
        author=book['author'],
        publication_date=datetime.strptime(str(book['year']), "%Y").date()
    )
