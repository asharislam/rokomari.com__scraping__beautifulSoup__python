import requests
from bs4 import BeautifulSoup

home_url = "https://www.rokomari.com/book"

req = requests.get(home_url)
"""print(req.status_code)"""
"""print(req.content)"""
soup = BeautifulSoup(req.content, "html.parser")
books = soup.find_all("div", class_="book-list-wrapper")
#print(books)

book_list = []

for book in books:
    book_title =book.find("p", class_="book-title").text
    book_author =book.find("p", class_="book-title").text
    book_price =book.find("p", class_="book-title").text
    book_dict ={
        "title": book_title.strip(),
        "author": book_author.strip(),
        "price": book_price.strip()
    }
    book_list.append(book_dict)

print(book_list)


