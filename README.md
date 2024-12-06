# LIMKOKWING UNIVERSITY LIBRARY MANGEMMENT SYSTEM
 OOP FINAL SEMESTER PROJECT
 
PROJECT PROPOSAL: LIBRARY MANAGEMENT SYSTEM
1.	Project Title

Library Management System for Limkokwing University

2.	Objectives

The main goal of this project is to design and implement a Library Management System that allows for efficient management of book records. The system will support CRUD (Create, Read, Update, and Delete) operations for handling books in the library's collection. The objectives include:
•	Implementing CRUD functionality for managing book records.

•	Designing an intuitive user interface with PyQt.

•	Using SQLite for managing book data and ensuring data integrity.

•	Collaborating as a team, following a software development methodology.

•	Producing clear documentation for both technical and user perspectives.

3.	Scope

The project will include the following functionalities:

•	Create: Users will be able to add new books with relevant details (title, author, ISBN, genre, publication year).
•	Read: The system will display the list of books and allow searching/filtering by title, author, ISBN, or genre.
•	Update: Users will be able to modify book records.

•	Delete: Users will be able to delete books from the system.

•	Search: Users will be able to search for books.

•	Clear Form: User will clear form.
 
The system will be developed using:

•	Frontend: PyQt for the graphical user interface.

•	Backend: SQLite for the database management.

•	Version Control: Git/GitHub for collaborative development and version management.
4.	Chosen Methodology

We follow the agile software development methodology for this project. Agile will allow for iterative development, enabling the team to produce functional prototypes in cycles and make improvements based on feedback. The methodology will help ensure flexibility in development and continuous progress.
•	Sprint Planning: The project will be divided into multiple sprints (e.g., one sprint for UI design, one for database design, etc.).
•	Daily Stand-ups: Short meetings will be held to discuss progress, obstacles, and next steps.
•	Iteration Reviews: At the end of each sprint, a review will be held to demonstrate the functionality implemented.
This methodology will promote effective collaboration and ensure that all members are aligned with the project goals.
 
5.	Timeline

The project will follow a timeline with specific milestones:

•	Day 1-5: Project Proposal & Requirements Analysis

•	Day 6-9: System Design (UML Diagrams, Database Schema)

•	Day 10-14: Frontend Development (PyQt User Interface)

•	Day 15-19: Backend Development (SQLite Integration, CRUD Operations)
•	Day 20-24: Testing and Debugging (Unit Tests, System Tests)

•	Day 25-29: Documentation (Technical & User Manual)

•	Day 30: Final Presentation and Submission

6.	Deliverables

The following deliverables will be submitted for the project:

•	Project Proposal: Detailed objectives, scope, methodology, and timeline.
•	System Design: UML diagrams (Class, Use Case) and database schema.

•	Implementation: Fully functional Library Management System with CRUD functionality.
•	Testing: Test cases for CRUD operations and documentation of results.

•	Documentation:

o	Technical Documentation: Explanation of system architecture, database schema, and code structure.
o	User Manual: Instructions for using the system.
 
7.	Resources

•	Software Tools:

o	PyQt for GUI development.

o	SQLite for database management.

o	Git/GitHub for version control.

o	IDE (PyCharm).

•	Hardware:

o	Personal computers for development and testing.

8.	Team Members and Roles

The team will be divided into the following roles:

•	Frontend Developer: Responsible for UI design and implementation using PyQt.
•	Backend Developer: Responsible for implementing CRUD operations and database management with SQLite.
•	Testing & Debugging: Responsible for testing the application and resolving issues.
•	Documentation: Responsible for preparing technical and user documentation.
 
9.	Evaluation Criteria

The project will be evaluated based on the following:

•	Effectiveness of the application in meeting the requirements (CRUD functionality, user interface, and database management).
•	Code quality, including proper use of object-oriented programming principles.
•	Design and usability of the user interface.

•	Completeness and clarity of documentation.

•	Team collaboration and individual contributions.
 

1.	Use Case Diagram
 
SYSTEM DESIGN
 
This diagram shows how users interact with the system, focusing on the different actions users can perform (CRUD operations).
Use Case Diagram for Library Management System:
•	Actors:
o	Admin (Primary User): Manages book records.
o	Guest/User: Can only view books (if applicable, optional functionality).
•	Use Cases:
o	Create Book: Admin can add new books to the system.
o	View Books: Admin and Guest can view all books.
o	Update Book: Admin can modify book details.
o	Delete Book: Admin can remove books from the system.
o	Search Books: Admin and Guest can search and filter books by title, author, genre, etc.
o	Clear: Admin clears form.
 
Use Case Diagram Example:



2.	Class Diagram
The class diagram represents the object-oriented design of the system, showing the classes and their relationships. This is where you define the entities (objects) and the operations (methods) they can perform.
Class Diagram for Library Management System:
•	Classes:
o	Book: Stores book details (title, author, ISBN, genre, etc.).
o	Library: Manages the list of books and CRUD operations (add, update, delete).
o	DatabaseHandler: Manages interaction with the SQLite database.
o	GUI: Manages the PyQt interface and user interactions.
 
Class Diagram Example:


Explanation of Classes:
•	Book Class:
o	Stores information about each book in the system.
o	Attributes include title, author, isbn, genre, and pubYear.
•	Library Class:
o	Manages a collection of Book objects.
o	Methods for adding, removing, updating, and searching books.
•	DatabaseHandler Class:
o	Manages database operations using SQLite (connecting to the database, executing queries).
 
•	GUI Class:
o	Responsible for the user interface built with PyQt.
o	Methods for displaying books, opening forms to add/update books, delete books, search books and handling user interactions.
 
IMPLEMENTATION OF THE LIBRARY MANAGEMENT SYSTEM
The implementation involve both the frontend (PyQt for GUI) and the backend (SQLite for the database). The key aspects include CRUD operations, integration of the database, and the user interface.
1.	Setup Development Environment
•	Python Installation: Ensure Python is installed (preferably Python 3.8 or later).
•	Required Libraries:
o	PyQt5: For building the graphical user interface (GUI).
o	sqlite3: For interacting with the SQLite database.
o	git: For version control.



2.	Database Setup (SQLite)
SQLite is used to store book information. The database schema have a single table books with the following fields:



The database is created and managed by a DatabaseManager class that will handle all database operations like adding, deleting, updating, and querying books.
 
3.	DatabaseManager Class
This class is responsible for handling all database operations. It have methods for connecting to the database and performing CRUD operations.
•	Methods:
o	create_book(): Adds a new book to the database.
o	update_book(): Updates an existing book record.
o	delete_book(): Deletes a book from the database.
o	get_all_books(): Retrieves all books from the database.
o	search_books(): Searches books by title, author, or genre.

4.	MAIN & LIBRARY UI Implementation (PyQt5)
The UI allow users to interact with the system. It will include the following components:
•	A main window showing all books.
•	A form to add a new book.
•	A form to update book details.
•	Buttons for CRUD operations.
•	About for information about the application.
•	Search bar for searching by title,author,ISBN and genere.
•	Clear button to clear the search bar field.


5.	CRUD Operations in the GUI
•	Add Book: When the user fills out the form and clicks the "Add Book" button, the information is inserted into the database.
•	Update Book: Implement functionality for updating a selected book from the table.
•	Delete Book: Implement functionality for deleting a selected book from the table.
•	Search: Use the search_books method from the DatabaseHandler class to filter books based on the search term.
 
6.	Testing
Once the system is implemented, testing will be essential to ensure everything works correctly. Test cases will include:
•	Adding, updating, and deleting books.
•	Searching and filtering the book list.
•	Ensuring the database properly updates with changes.


4.	User Interface Design for Library Management System
The user interface (UI) of the Library Management System (LMS) is a critical component for ensuring a seamless and intuitive user experience. In this section, we design a UI using PyQt5, focusing on creating an easy-to-use and visually appealing layout that enables users to manage book records (CRUD operations), search for books, and view the book details.

Key UI Components
The UI consist of the following primary components:
1.	Search Bar: A text input field to allow users to search for books by title, author, ISBN, or genre.
2.	Table for Displaying Books: A table to show the list of books available in the library, with columns like ID, Title, Author, ISBN, Genre, and Year.
3.	Book Form: A form for adding or updating book records, including fields for the book's title, author, ISBN, genre, and publication year.
4.	Buttons for CRUD Operations: Buttons for adding, updating, deleting, and searching for books.
5.	About: For understanding the application.
Design Principles
•	Clarity: The UI is simple and intuitive, with clear labels and instructions.
•	Consistency: Consistent fonts, colors, and layouts across the application.
•	Responsiveness: The UI adapt to different screen sizes and ensure easy navigation.
•	Error Handling: Provide meaningful error messages and form validation to guide users.
 
Detailed UI Layout
1.	Main Window Layout: The main window have a vertical layout, containing:
o	A search bar at the top to filter books by keyword.
o	A table to display books retrieved from the database.
o	A form below the table to add new books or update existing ones.
o	Buttons for performing CRUD operations.
2.	Search Bar: The search bar will allow users to enter search terms like the book title, author, genre, or ISBN. As the user types, the book list will automatically filter based on the entered text.

3.	Book Table: The table will display all the books in the library, showing relevant information such as:
o	Book ID (auto-generated by the database)
o	Title
o	Author
o	ISBN
o	Genre
o	Year
The table will allow users to select rows for updating or deleting books.


4.	Add/Update Book Form: This form will have input fields for entering the book's title, author, ISBN, genre, and publication year. This form will be used both for adding new books and updating existing ones.
5.	Action Buttons:
o	Add Book: A button to add a new book to the library.
o	Update Book: A button to update an existing book's details.
o	Delete Book: A button to delete a selected book from the library.
o	Search: A button to search for books based on the entered search term.
o	Clear Form: A button used to clear the form input fields.
o	Clear Button: Use for clearing search bar.
 
WIREFRAME MOCKUP



 
 


 
 


 
 


 
 
 
PyQt5 Implementation for UI
The PyQt5 implementation for the UI can be broken down into the following sections:
1.	Search Bar: The search bar will filter the table based on the entered text (title, author, or genre).

2.	Table Widget: This will display the books in the database. We will populate the table with data fetched from the DatabaseManager.
3.	Add/Update Form: The form will be used for entering or updating book information. Each input field corresponds to a book attribute (title, author, ISBN, genre, year).
4.	Buttons: Buttons for adding, updating, and deleting books will be placed under the form and connected to their respective functions
Final UI Features
•	Search Functionality: As the user types into the search bar, the book list will filter automatically.
•	Clear Search Bar: Clears the search bar after a user is done search.
•	CRUD Operations:
o	Add Book: When the "Add Book" button is clicked, the form's data will be sent to the backend to insert the new book.
o	Update Book: After selecting a book from the table, the form fields will be populated with the book's information, allowing the user to modify it.
o	Delete Book: When a user selects a book from the table and clicks "Delete", the selected book will be removed from the database.
 
DATABASE MANAGEMENT FOR LIBRARY MANAGEMENT SYSTEM
The Database Management section of the Library Management System (LMS) focuses on creating, managing, and organizing the database to store book records. The system will use SQLite, a lightweight, serverless relational database, to handle book information efficiently.

Database Design Overview
The database will consist of a single table to manage the book records and provide functionalities for CRUD operations (Create, Read, Update, and Delete). The table will store key attributes such as the book title, author, ISBN, genre, and publication year.
Database Structure
•	Database Engine: SQLite
•	Table: books
•	Fields:
o	ID (Primary Key): Unique identifier for each book (auto- incremented).
o	Title: The title of the book.
o	Author: The author(s) of the book.
o	ISBN: International Standard Book Number (unique identifier for the book).
o	Genre: The genre of the book (e.g., fiction, non-fiction, mystery, etc.).
o	Publication Year: The year the book was published.
 
Table Schema
Below is the SQL schema for creating the books table in the SQLite database:

•	id: The primary key will automatically increment with each new entry, ensuring that each book has a unique identifier.
•	title, author, genre: Text fields for storing the book’s title, author, and genre.
•	isbn: A unique field to ensure that each book is identified uniquely by its ISBN.
•	publication_year: An integer field to store the year of publication.
Database Operations (CRUD)
The application will interact with the database through the following CRUD operations, which are implemented in Python using SQLite3 library.
1.	Create: Add a new book to the database.
2.	Read: Fetch book details from the database (list all books, search by title, author, ISBN, or genre).
3.	Update: Modify an existing book’s details.
4.	Delete: Remove a book from the database
 
CRUD Operations in Detail
1.	Create (Add a New Book)
The Create operation will insert a new book record into the database. The data will be collected from the user through the PyQt UI (Add Book form).

2.	Read (View/Search Books)
The Read operation will fetch all books or search books by specific attributes like title, author, ISBN, or genre.

3.	Update (Modify an Existing Book)
The Update operation will allow users to modify an existing book record by updating fields such as title, author, ISBN, genre, or publication year.
4.	Delete (Remove a Book)
The Delete operation will remove a book from the database by its unique identifier (ID).
Database Interaction with PyQt
The PyQt user interface will interact with these database functions by calling them when the user performs actions such as adding, updating, or deleting books. For example, when the "Add Book" button is clicked, the following code will collect the form data and call the add_book() function:
Testing Database Operations
To ensure that the database functions correctly, a Test Plan was created, which will include test cases for each CRUD operation. The test cases ensure the following:
•	The database correctly inserts, updates, and deletes records.
•	Data is displayed properly in the PyQt table.
•	Search functionality retrieves relevant books.
•	Database connections are closed properly after operations.
Example Test Cases:
1.	Test Case 1: Add Book
o	Input: Title = "Book One", Author = "Author A", ISBN = "12345", Genre = "Fiction", Year = 2020
 
o	Expected Output: Book is added to the database, and the table updates to display the new book.
2.	Test Case 2: Search Book
o	Input: Search for "Fiction"
o	Expected Output: The table displays all books in the "Fiction" genre.
3.	Test Case 3: Update Book
o	Input: Update the author of "Book One" to "Author B"
o	Expected Output: The book's author is updated in the database, and the table reflects the change.
4.	Test Case 4: Delete Book
o	Input: Delete the book with ID = 1
o	Expected Output: The book is removed from the database and the table updates to reflect the deletion.

6.	Testing and Debugging for Library Management System
Testing and debugging were crucial parts of ensuring that the Library Management System (LMS) functions correctly, user-friendly, and free of errors. This section outlines the testing strategies, test cases, and debugging techniques for the project.

6.1	Testing Approach
The testing process for the Library Management System will include different levels of testing:
1.	Unit Testing: Focuses on individual functions, such as adding, updating, or deleting books from the database. Unit tests will ensure that each function behaves as expected.
2.	Integration Testing: Tests how well the components of the system (PyQt UI and SQLite database) work together. It ensures that the interactions between the database and the user interface (UI) are seamless.
 
3.	Functional Testing: Ensures that the application meets all the functional requirements specified in the project proposal, such as adding, updating, deleting, and searching for books.
4.	User Interface Testing: Ensures that the PyQt UI is user-friendly, easy to navigate, and responsive. It tests if the UI components (buttons, forms, tables) function correctly when interacted with.
5.	Regression Testing: Ensures that new changes or additions to the application don't break existing features.

6.2	Testing Plan
The testing plan outline test cases for each core functionality of the Library Management System. The tests focuses on the CRUD operations, UI functionality, and database interactions.
Test Case 1: Add Book (Create)
•	Test Objective: Verify that a new book can be added to the database.
•	Steps:
1.	Open the "Add Book" form in the UI.
2.	Enter the following details:
	Title: "The Great Gatsby"
	Author: "F. Scott Fitzgerald"
	ISBN: "9780743273565"
	Genre: "Fiction"
	Publication Year: 1925
3.	Click "Add Book".
•	Expected Result: The book should be added to the database. The table should display the new book.
•	Actual Result: To be filled during testing.
•	Pass/Fail: To be determined.
 
Test Case 2: Update Book (Modify)
•	Test Objective: Verify that existing book details can be updated.
•	Steps:
1.	Select a book from the list.
2.	Click on the "Edit" button next to the book.
3.	Update the title, e.g., change "The Great Gatsby" to "Gatsby's Adventure".
4.	Click "Update".
•	Expected Result: The book's title should be updated in the database, and the updated title should be visible in the table.
•	Actual Result: To be filled during testing.
•	Pass/Fail: To be determined.
Test Case 3: Delete Book (Remove)
•	Test Objective: Verify that a book can be deleted from the system.
•	Steps:
1.	Select a book from the list.
2.	Click on the "Delete" button next to the book.
3.	Confirm the deletion.
•	Expected Result: The book should be removed from the database, and the table should update to reflect the deletion.
•	Actual Result: To be filled during testing.
•	Pass/Fail: To be determined.
Test Case 4: Search Book (Read)
•	Test Objective: Verify that the search functionality works for different attributes (e.g., title, author, genre).
•	Steps:
1.	Enter the search term "Fiction" in the search field.
2.	Click "Search".
•	Expected Result: The table should display books that match the search term (in this case, books with the genre "Fiction").
•	Actual Result: To be filled during testing.
•	Pass/Fail: To be determined.
 
Test Case 5: UI Responsiveness
•	Test Objective: Verify that the user interface is responsive and user- friendly.
•	Steps:
1.	Open the application and resize the window.
2.	Interact with various UI components (e.g., buttons, input fields, table).
•	Expected Result: The UI should adjust properly, and all components should be clickable and functional without layout issues.
•	Actual Result: To be filled during testing.
•	Pass/Fail: To be determined.
Test Case 6: Database Integrity
•	Test Objective: Verify that the database maintains integrity after CRUD operations.
•	Steps:
1.	Add a new book.
2.	Update the book.
3.	Delete the book.
4.	Check the database for the book's record.
•	Expected Result: The book should be properly added, updated, and removed from the database.
•	Actual Result: To be filled during testing.
•	Pass/Fail: To be determined.
 
6.3	Debugging Process
During the testing phase, any issues identified will need to be debugged to ensure the system runs smoothly. The debugging process will involve the following steps:
1.	Identifying the Issue:
o	Review the test case that failed and check for error messages or logs.
o	Check the application’s behavior to identify what’s not working as expected.
2.	Isolating the Problem:
o	Check if the problem is related to the UI, database, or both.
o	Verify if the issue is a logic error (e.g., incorrect calculations, logic flow) or a UI rendering issue (e.g., incorrect layout).
3.	Using Debugging Tools:
o	Use Python's built-in pdb (Python Debugger) for step-by-step debugging of code.
o	Use PyQt’s debugging tools (e.g., qDebug()) to trace UI-related issues.
4.	Fixing the Bug:
o	Once the issue is identified, modify the code to correct the problem.
o	If it's a database-related issue, check SQL queries for correctness (e.g., syntax errors or incorrect use of variables).
5.	Re-testing:
o	After fixing the issue, re-run the test cases to confirm that the bug has been resolved and that no new issues have been introduced.
6.4	Debugging Example
Issue: The "Add Book" functionality fails to add a book to the database.
1.	Step 1: Check the error logs. The error message says there is an issue with the INSERT INTO SQL query.
 
2.	Step 2: Review the SQL query in the code. It turns out that the isbn field is mistakenly being passed as None, which violates the NOT NULL constraint in the database.
3.	Step 3: Modify the code to ensure the isbn is correctly passed before the query is executed.
4.	Step 4: Re-test the "Add Book" functionality. The book is successfully added to the database.
6.5	Regression Testing
Once the necessary changes are made, regression testing will be performed to ensure that no previous functionality has been broken due to recent changes or fixes. This will include rerunning the previously passed test cases after each modification to verify overall system stability.

7.	Documentation for Library Management System
Documentation plays a vital role in ensuring that the system is understandable, maintainable, and usable. For the Library Management System (LMS) project, comprehensive documentation will be divided into several sections: Technical Documentation, User Manual, and References.

7.1	Technical Documentation
The Technical Documentation provides an in-depth explanation of the system’s architecture, components, and implementation. This documentation is mainly intended for developers and system maintainers.
7.1.1	System Architecture
The system consists of two major components:
1.	Front-End (User Interface): Built using PyQt, it allows users to interact with the library system. The front-end communicates with the back-end via function calls to the database.
2.	Back-End (Database Management): Uses SQLite to store and manage the library's book records. The database is integrated with the PyQt UI for CRUD operations.
 
7.1.2	Database Schema
The database schema will define the structure of the SQLite database used to store book records. The primary table for storing book information will be as follows:
•	Books Table:
o	id (INTEGER, Primary Key, Autoincrement)
o	title (TEXT, NOT NULL)
o	author (TEXT, NOT NULL)
o	isbn (TEXT, UNIQUE, NOT NULL)
o	genre (TEXT)
o	publication_year (INTEGER)
The system will use SQL queries to interact with the database, with functions for adding, updating, deleting, and reading book records.
7.1.3	Code Architecture
The code will follow Object-Oriented Programming (OOP) principles, with classes representing different entities in the system. Some of the main classes are:
•	Book Class:
o	Attributes: title, author, ISBN, genre, publication_year.
o	Methods: add_book(), update_book(), delete_book(), get_books().
•	Library Class:
o	Methods: handle CRUD operations, communicate with SQLite, manage book records.
The application will use the PyQt framework for the front-end, with event-driven programming to handle UI interactions (e.g., button clicks, form submissions).
 
7.1.4	File Structure
The project have a clean, modular file structure to organize the code and resources:

/LIMKOKWING UNIVERSITY LIBRARY MANAGEMENT SYSTEM
│
├── CODE/pythonProject	#folder containting(main.py,library_ui.py and _.pr
├── README.md	# Project overview and setup instructions
The system will include error-handling mechanisms to manage database connection issues, missing inputs, and invalid user actions. These will include:
•	Displaying user-friendly error messages.
•	Logging errors to a file for later review.
•	Validating inputs before performing database operations.
 
USER MANUAL
The User Manual is designed to help end-users understand how to interact with the Library Management System. This documentation will include detailed instructions on how to use the application, from installing the system to performing CRUD operations.
Installation Instructions
•	Pre-requisites:
o	Python 3.x
o	PyQt5 library
o	SQLite (built-in with Python)
Steps for Installation:
1.	Clone the repository from GitHub.
2.	Install the required dependencies: pip install pyqt5 sqlite3
3.	Run the main application file: python main.py
Using the Application Home Screen:
•	The main window will display a table with existing books in the library.
•	The user can interact with the buttons for CRUD operations:
o	Add Book: Opens a form to add a new book.
o	Edit Book: Allows modification of the selected book's details.
o	Delete Book: Deletes the selected book.
o	Search Book: Filters the displayed books based on search criteria (title, author, genre).
o	Clear Form: Clears the input fields.
o	Clear: Clears the search bar field.
Add a Book:
1.	Click the "Add Book" button.
2.	Fill in the details (title, author, ISBN, genre, publication year).
3.	Click "Save".
 
Update Book:
1.	Select a book from the list.
2.	Click "Edit" and modify the details.
3.	Click "Update" to save changes.
Delete a Book:
1.	Select a book.
2.	Click "Delete" to remove it from the database.
Search Books:
1.	Enter search criteria (e.g., title, author, or genre).
2.	Click the "Search" button to filter the list.
Clear Form:
1.	Click the "Clear form" button to clear the form.


Troubleshooting
•	Issue: The application crashes upon launching.
o	Solution: Ensure all dependencies (PyQt5, SQLite) are installed correctly. Check the main.py file for any missing imports.
•	Issue: Book not added to the database.
o	Solution: Make sure all required fields (title, author, ISBN) are filled in the "Add Book" form.
•	Issue: The search doesn't return any results.
o	Solution: Ensure the search criteria match the database records (case-sensitive).
 
References
The References section includes the resources and documentation that we used during the development of the system.
1.	PyQt5 Documentation: https://riverbankcomputing.com/software/pyqt/intro
2.	SQLite Documentation: https://www.sqlite.org/docs.html
3.	Python OOP Tutorial: https://realpython.com/python3-object-oriented- programming/
4.	GitHub: LansanaAlfredBraima/LIMKOKWING-UNIVERSITY-LIBRARY-MANGEMMENT-SYSTEM: OOP FINAL SEMESTER PROJECT
5.	SQLite Python Library: https://pypi.org/project/sqlite3/
