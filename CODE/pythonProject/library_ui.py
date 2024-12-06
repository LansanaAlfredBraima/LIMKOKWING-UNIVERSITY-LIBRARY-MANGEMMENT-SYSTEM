from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit, QPushButton, QTabWidget,
    QLabel, QFrame, QMessageBox, QSpacerItem, QSizePolicy, QTableWidget, QTableWidgetItem, QHeaderView
)
from PyQt5.QtCore import Qt
from database_manager import DatabaseManager


class LibraryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Library Management System")
        self.setGeometry(100, 100, 1000, 700)
        self.setStyleSheet("background-color: #32CD32; color: white; font-family: Arial; font-size: 14px;")

        main_layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""QTabWidget::pane { border: 1px solid #555; }
            QTabBar::tab { background-color: #1976D2; color: white; padding: 10px; margin-right: 10px; border-radius: 5px; }
            QTabBar::tab:selected { background-color: #1565C0; }
            QTabBar::tab:hover { background-color: #0D47A1; }
        """)
        main_layout.addWidget(self.tabs)

        self.manage_books_tab = QWidget()
        self.about_tab = QWidget()

        self.tabs.addTab(self.manage_books_tab, "Manage Books")
        self.tabs.addTab(self.about_tab, "About")

        self.setup_manage_books_tab()
        self.setup_about_tab()

        self.setLayout(main_layout)

    def setup_manage_books_tab(self):
        layout = QVBoxLayout()

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.clear_search_button = QPushButton("Clear")

        self.search_input.setFixedWidth(200)
        self.search_button.setFixedWidth(100)
        self.clear_search_button.setFixedWidth(100)

        self.search_input.setStyleSheet("background-color: white; color: black; padding: 8px; border-radius: 5px;")
        self.search_button.setStyleSheet(self.get_button_style())
        self.clear_search_button.setStyleSheet(self.get_button_style())

        search_layout.addWidget(QLabel(""))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        search_layout.addWidget(self.clear_search_button)
        search_layout.setAlignment(Qt.AlignCenter)
        layout.addLayout(search_layout)

        form_frame = QFrame()
        form_frame.setStyleSheet("background-color: #333; border-radius: 10px; padding: 20px;")
        form_layout = QFormLayout(form_frame)

        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.isbn_input = QLineEdit()
        self.genre_input = QLineEdit()
        self.year_input = QLineEdit()

        self.title_input.setStyleSheet("background-color: white; color: black; padding: 8px; border-radius: 5px;")
        self.author_input.setStyleSheet("background-color: white; color: black; padding: 8px; border-radius: 5px;")
        self.isbn_input.setStyleSheet("background-color: white; color: black; padding: 8px; border-radius: 5px;")
        self.genre_input.setStyleSheet("background-color: white; color: black; padding: 8px; border-radius: 5px;")
        self.year_input.setStyleSheet("background-color: white; color: black; padding: 8px; border-radius: 5px;")

        form_layout.addRow("Title:", self.title_input)
        form_layout.addRow("Author:", self.author_input)
        form_layout.addRow("ISBN:", self.isbn_input)
        form_layout.addRow("Genre:", self.genre_input)
        form_layout.addRow("Year:", self.year_input)

        form_layout_wrapper = QHBoxLayout()
        form_layout_wrapper.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        form_layout_wrapper.addWidget(form_frame)
        form_layout_wrapper.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(form_layout_wrapper)

        button_layout = QHBoxLayout()
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.add_button = QPushButton("Add Book")
        self.update_button = QPushButton("Update Book")
        self.delete_button = QPushButton("Delete Book")
        self.clear_form_button = QPushButton("Clear Form")

        self.add_button.setStyleSheet(self.get_button_style())
        self.update_button.setStyleSheet(self.get_button_style())
        self.delete_button.setStyleSheet(self.get_button_style())
        self.clear_form_button.setStyleSheet(self.get_button_style())

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.clear_form_button)
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        layout.addLayout(button_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Title", "Author", "ISBN", "Genre", "Year"])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setColumnHidden(0, True)
        self.table.setStyleSheet("""
            QTableWidget { background-color: white; color: black; }
            QHeaderView::section { background-color: #1976D2; color: white; padding: 5px; }
        """)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        table_layout = QHBoxLayout()
        table_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        table_layout.addWidget(self.table)
        table_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(table_layout)

        self.manage_books_tab.setLayout(layout)

        self.add_button.clicked.connect(self.add_book)
        self.update_button.clicked.connect(self.update_book)
        self.delete_button.clicked.connect(self.delete_book)
        self.search_button.clicked.connect(self.search_books)
        self.clear_search_button.clicked.connect(self.clear_search)
        self.clear_form_button.clicked.connect(self.clear_form)

        self.update_table()
        self.table.selectionModel().selectionChanged.connect(self.populate_form_from_table)

    def setup_about_tab(self):
        layout = QVBoxLayout()
        about_label = QLabel("<h2>Library Management System</h2><p>Version: 1.0</p><p>Developed by XYZ</p>")
        layout.addWidget(about_label)
        self.about_tab.setLayout(layout)

    def get_button_style(self):
        return """
            background-color: #1976D2; color: white; padding: 10px; border-radius: 5px;
            font-weight: bold; font-size: 14px; margin: 5px;
        """

    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        isbn = self.isbn_input.text()
        genre = self.genre_input.text()
        year = self.year_input.text()

        if not all([title, author, isbn, genre, year]):
            self.show_message("Error", "Please fill in all fields.")
            return

        # Add book to the database
        self.db.add_book(title, author, isbn, genre, year)

        # Show success message
        self.show_message("Success", "Book added successfully.")

        # Clear form and update table
        self.clear_form()
        self.update_table()

    def update_book(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            self.show_message("Error", "Please select a book to update.")
            return

        book_id = self.table.item(selected_row, 0).text()
        title = self.title_input.text()
        author = self.author_input.text()
        isbn = self.isbn_input.text()
        genre = self.genre_input.text()
        year = self.year_input.text()

        if not all([title, author, isbn, genre, year]):
            self.show_message("Error", "Please fill in all fields.")
            return

        # Update book in the database
        self.db.update_book(book_id, title, author, isbn, genre, year)

        # Show success message
        self.show_message("Success", "Book updated successfully.")

        # Clear form and update table
        self.clear_form()
        self.update_table()

    def delete_book(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            self.show_message("Error", "Please select a book to delete.")
            return

        book_id = self.table.item(selected_row, 0).text()

        # Delete book from the database
        self.db.delete_book(book_id)

        # Show success message
        self.show_message("Success", "Book deleted successfully.")

        # Update table
        self.update_table()

    def search_books(self):
        search_term = self.search_input.text()
        if search_term:
            books = self.db.search_books(search_term)
        else:
            books = self.db.get_all_books()
        self.populate_table(books)

    def clear_search(self):
        self.search_input.clear()
        self.update_table()

    def clear_form(self):
        self.title_input.clear()
        self.author_input.clear()
        self.isbn_input.clear()
        self.genre_input.clear()
        self.year_input.clear()

    def populate_table(self, books):
        self.table.setRowCount(0)
        for book in books:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            for col, value in enumerate(book):
                self.table.setItem(row_position, col, QTableWidgetItem(str(value)))

    def update_table(self):
        books = self.db.get_books()
        self.populate_table(books)

    def populate_form_from_table(self):
        selected_row = self.table.currentRow()
        if selected_row != -1:
            self.title_input.setText(self.table.item(selected_row, 1).text())
            self.author_input.setText(self.table.item(selected_row, 2).text())
            self.isbn_input.setText(self.table.item(selected_row, 3).text())
            self.genre_input.setText(self.table.item(selected_row, 4).text())
            self.year_input.setText(self.table.item(selected_row, 5).text())

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()
