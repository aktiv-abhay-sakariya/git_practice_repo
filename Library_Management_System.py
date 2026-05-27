class Book:
    def __init__(self, book_id, book_title, book_author):
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.is_issued = False

    def display(self):
        """
        Display Book information
        """
        print('---'*10)
        status = "Available" if not self.is_issued else 'Not-Available'
        print('Book ID :', self.book_id)
        print('Book Title :', self.book_title)
        print('Book Author Name :', self.book_author)
        print('Book Status :', status)


class Member:
    def __init__(self, member_id, member_name):
        self.member_id = member_id
        self.member_name = member_name
        self.issue_book = []

    def add_book(self, book):
        """
        Add Book in member issue book list when issue book

        Args:
            book (obj) : book object which is issue by member
        """
        if book not in self.issue_book:
            self.issue_book.append(book)
        else:
            print('Book Already Issued')

    def remove_book(self, book):
        """
        Remove Book in member issue book list when return book

        Args:
            book (obj) : book object which is return by member
        """
        if book in self.issue_book:
            self.issue_book.remove(book)
        else:
            print('Book Already Returned')

    def display(self):
        """
        Display member information
        """
        print('---'*10)
        print('Member ID :', self.member_id)
        print('Member Name :', self.member_name)
        print('Total Books Issue :', len(self.issue_book))


class Library(Book, Member):
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []
        self.members = []
        while True:
            print('\n---- MAIN MENU ----')
            print("""\n1. Add Books\n2. Add Members\n3. Display All Books\n4. Display All Member\n5. Issue Book\n6. Return Book\n7. Search Book\n8. Exit""")
            choice = self.safe_choice(8)
            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.add_member()
            elif choice == 3:
                self.list_books()
            elif choice == 4:
                self.list_members()
            elif choice == 5:
                self.issue_book()
            elif choice == 6:
                self.return_book()
            elif choice == 7:
                self.search_book()
            else:
                print('\nThank You')
                break

    def safe_choice(self, limit):
        """
        Repeatedly ask number from user until enter between 1 to limit

        argument:
            limit (int): in the sequence last number user can enter

        return:
            select : int which user are enter
        """
        while True:
            try:
                select = int(input('\nEnter No :'))
                if 1 <= select <= limit:
                    break
                print('\nEnter 1 to', limit)
            except Exception:
                print('\nEnter Only Number')
        return select

    def safe_input(self, msg):
        """
        Continuously prompts the user for input until a non-blank string is entered

        Args:
            msg (string): The prompt message displayed to the user

        Returns:
            string: string with strip and non-blank entered by the user
        """
        while True:
            user_input = input(msg).strip()
            if user_input:
                break
            print('\nDo not enter blank')
        return user_input

    def ask_next_iter(self, msg):
        """
        Continuously prompts the user for input until a 'y' or 'n' string is entered

        Args:
            msg (string): The prompt message displayed to the user

        Returns:
            string: string 'y' or 'n'
        """
        while True:
            user_input = self.safe_input(msg).strip()
            if user_input.lower() in ('y', 'n'):
                break
            print("\nEnter only 'y' or 'n'")
        return user_input.lower()

    def add_book(self):
        """
        Add book information using book class and store their object
        """
        while True:
            book_id = self.safe_input('Enter Book ID :')
            check_book = list(filter(lambda book: book.book_id == book_id, self.books))
            if check_book:
                print('Book Id already Added')
                continue
            book_title = self.safe_input('Enter Book Title :')
            book_author = self.safe_input('Enter Book Author name :')
            self.books.append(Book(book_id, book_title, book_author))
            print('\nBook Added')
            next_iter = self.ask_next_iter('Do you want add another book (enter Y/N) ?')
            if next_iter == 'n':
                break

    def add_member(self):
        """
        Add member information using member class and store their object
        """
        while True:
            member_id = self.safe_input('Enter Member ID :')
            check_member = list(filter(lambda member: member.member_id == member_id, self.members))
            if check_member:
                print('Member Id already Added')
                continue
            member_name = self.safe_input('Enter Member Name :')
            self.members.append(Member(member_id, member_name))
            print('\nMember Added')
            next_iter = self.ask_next_iter('Do you want add another book (enter Y/N) ?')
            if next_iter == 'n':
                break

    def list_books(self):
        """
        Display information of all books
        """
        if self.books:
            for book in self.books:
                book.display()
        else:
            print('\nBooks Not Add Yet')

    def list_members(self):
        """
        Display information of all member
        """
        if self.members:
            for member in self.members:
                member.display()
        else:
            print('\nMembers Not Add Yet')

    def issue_book(self):
        """
        Issue book or store book object in member issue book list
        """
        book_id = self.safe_input('Enter Book ID :')
        member_id = self.safe_input('Enter Member ID :')
        check_book = list(filter(lambda book: book.book_id == book_id and not book.is_issued, self.books))
        check_member = list(filter(lambda member: member.member_id == member_id, self.members))
        if check_book and check_member:
            check_member[0].add_book(check_book[0])
            check_book[0].is_issued = True
            print('\nBook Issued')
        else:
            print('\nBook or Member not found or book already issue')

    def return_book(self):
        """
        Return book or remove book object in member issue book list
        """
        book_id = self.safe_input('Enter Book ID :')
        member_id = self.safe_input('Enter Member ID :')
        check_book = list(filter(lambda book: book.book_id == book_id and book.is_issued, self.books))
        check_member = list(filter(lambda member: member.member_id == member_id and check_book[0] in member.issue_book, self.members))
        if check_book and check_member:
            check_member[0].remove_book(check_book[0])
            check_book[0].is_issued = False
            print('\nBook Returned')
        else:
            print('\nBook or Member not found or book already return')

    def search_book(self):
        """
        Search book by title and Display That Book information
        """
        book_title = self.safe_input('Enter Book title :')
        check_book = list(filter(lambda book: book.book_title == book_title, self.books))
        if check_book:
            for book in check_book:
                book.display()
        else:
            print('\nBook not found')


if __name__ == '__main__':
    libary = Library('public')
