# Create a list of favorite books with book titles and authors
fav_books = [{
    "title": "the Legend",
    "author": "vikram"
}, {
    "title": "Ghazi",
    "author": "George"
}, {
    "title": "come and rock",
    "author": "suresh"
}, {
    "title": "The lazy boy",
    "author": "john"
}, {
    "title": "jhansi",
    "author": "rathod"
}]

# Use list slicing to print the first three books in the list
first_three_fav_books = fav_books[:3]
print("my First three favorite books:")
for book in first_three_fav_books:
  print(f"{book['title']} by {book['author']}")

# Create a dictionary representing a basic student database
student_info = {
    "student_id": 123,
    "first_name": "smatil",
    "last_name": "boddu",
    "email": "smatil.boddu@gmail.com",
    "courses": ["biology", "physics", "Science"]
}


def test_fav_books():
  assert fav_books[1]['title'] == "Ghazi"
  assert isinstance(fav_books, list)

  assert isinstance(student_info, dict)
  assert student_info["first_name"] == "smatil"
