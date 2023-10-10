# creating the class "library" with some functions which are going to act from the library side

class library:
  def __init__(self,book):
    self.book_list = book
  def show(self):
    print(*self.book_list)
  def lend_book(self,book_name):
    if book_name in self.book_list:
      self.book_list.remove(book_name)
      print('Book issued. Happy Learning. Thank you.')
      return True
    else:
      print("Sorry! This book is not availabe.")
      return False
  def returnBook(self,book_name):
    self.book_list.append(book_name)
    return True

# creating the class "customer" with some functions which are going to act from the library side

class customer:
  def __init__(self):
    self.bookList = []
  def add_book(self,book_name):
    self.bookList.append(book_name)
  def show(self):
    print(self.bookList)
  def request_book(self):
    print('Enter the book name to checkout:')
    self.book = input()
    return self.book
  def return_book(self):
    print('Enter the book name to checkin:')
    self.book = input()
    return self.book
  def lend_book_to_lib(self,book_name):
    if book_name in self.bookList:
      self.bookList.remove(book_name)
      print('You have successfully returned your',book_name,'book. Thank you.')
      Status=lib_cbe.returnBook(book_name)
      return True
    else:
      print("You are trying to return the wrong book. Please check your book.")

# creating the object "lib_cbe" for the class "library" with some arguments

lib_cbe = library(['book1','book2','book3','book4','book5','book2'])

# creating the object "aravinth" for the class "customer" with some arguments

aravinth = customer()


while True:
  print('-----------------------------------------------------------------------------')
  print("Choose the option from the below list:")
  print("1 - Show the list of books \n2 - Lend a book from the library \n3 - Borrow the book\n4 - Return the Book\n0 - Exit")
  option = int(input("Enter your option here:"))
  if option == 1:
    lib_cbe.show()
  elif option == 2:
    requested_book = aravinth.request_book()
    status = lib_cbe.lend_book(requested_book)
    if status == True:
      aravinth.add_book(requested_book)
  elif option == 3:
    aravinth.show()
  elif option == 4:
    returned_book = aravinth.return_book()
    status=aravinth.lend_book_to_lib(returned_book)
  elif option == 0:
    break