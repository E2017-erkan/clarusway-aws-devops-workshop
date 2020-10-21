# remove duplicate from given_list using list comprehension
list_books= ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby","One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea","One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World","I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby","One Hundred Years of Solitude", "Pride and Prejudice"]for i in list_books: 
    x = list_books.count(i) 
    if x == 1:
        print(i)