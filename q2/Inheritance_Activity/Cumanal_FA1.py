
# Library Management System

class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    # Setters
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        Publication.__init__(self, title, author)
        self.__number_of_pages = number_of_pages

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages <= 0:
            print("The number of pages must be positive.")
        else:
            self.__number_of_pages = number_of_pages

    def display_info(self):
        Publication.display_info(self)
        print("Number of pages:", self.__number_of_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        Publication.__init__(self, title, author)
        self.__issue_number = issue_number

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number <= 0:
            print("The issue number must be positive.")
        else:
            self.__issue_number = issue_number

    def display_info(self):
        Publication.display_info(self)
        print("Issue number:", self.__issue_number)


# Creating objects
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)


# Displaying information
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.display_info()

print("\nMagazine Information:")
mag1.display_info()
