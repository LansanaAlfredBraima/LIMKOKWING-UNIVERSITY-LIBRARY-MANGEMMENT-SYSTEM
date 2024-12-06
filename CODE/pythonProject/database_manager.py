import sqlite3

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect('library.db')
        self.cursor = self.connection.cursor()
        self.create_books_table()

    def create_books_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            isbn TEXT,
            genre TEXT,
            year INTEGER
        )''')
        self.connection.commit()

    def add_book(self, title, author, isbn, genre, year):
        self.cursor.execute('''INSERT INTO books (title, author, isbn, genre, year)
                               VALUES (?, ?, ?, ?, ?)''', (title, author, isbn, genre, year))
        self.connection.commit()

    def update_book(self, book_id, title, author, isbn, genre, year):
        self.cursor.execute('''UPDATE books SET title=?, author=?, isbn=?, genre=?, year=? 
                               WHERE id=?''', (title, author, isbn, genre, year, book_id))
        self.connection.commit()

    def delete_book(self, book_id):
        self.cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
        self.connection.commit()

    def search_books(self, search_term):
        self.cursor.execute(
            '''SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ? OR genre LIKE ?''',
            ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))
        return self.cursor.fetchall()

    def get_books(self):
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()
