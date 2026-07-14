class Book:

    def __init__(self, title, author, num_of_pages):
        self.title = title
        self.authour = author
        self.num_of_pages = num_of_pages

    def __str__(self):
        return f"'{self.title}' by {self.authour}"
    
    def __eq__(self, other):
        return self.title == other.title and self.authour == other.author
    
    def __lt__(self, other):
        return self.num_of_pages < other.num_of_pages

    def __gt__(self, other):
        return self.num_of_pages > other.num_of_pages
    
    def __add__(self, other):
        return self.num_of_pages + other.num_of_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.authour
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.authour
        elif key == "num_of_pages":
            return self.num_of_pages
        else:
            return f"Key {key} was not found"
    
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion, The Witch and The Wardrobe", "C.S. Lewis", 172)

print(book1) #__str__
print(book1 == book2) #__eq__
print(book2 < book3) #__lt__
print(book2 > book3) #__gt__
print(book1 + book2) #__add__
print("Lion" in book3) #__contains__
print(book1['title']) #__getitem__
print(book1["author"]) # __getitem__
print(book1['num_of_pages']) #__getitem__
