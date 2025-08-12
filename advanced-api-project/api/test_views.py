# api/test_views.py

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Author, Book

User = get_user_model()

class BookAPITest(APITestCase):
    """
    We are telling the program to create a new test case for the Book API.
    This class will contain all the tests for our Book-related endpoints.
    """
    def setUp(self):
        """
        We are setting up the initial data for our tests.
        This runs before every single test method in this class.
        """
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=self.author, publication_year=1997)
        self.book2 = Book.objects.create(title="Fantastic Beasts and Where to Find Them", author=self.author, publication_year=2001)

    # --- Test CRUD Operations (Read-only) ---

    def test_list_books_unauthenticated(self):
        """
        We are testing that an unauthenticated user can view the list of books.
        """
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # We are telling the program to check that the response contains our two test books.
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_unauthenticated(self):
        """
        We are testing that an unauthenticated user can view a single book.
        """
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # We are telling the program to check that the title of the returned book is correct.
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_unauthenticated_fails(self):
        """
        We are testing that an unauthenticated user cannot create a book.
        Because the permissions are IsAuthenticatedOrReadOnly, a POST request should be denied.
        """
        data = {'title': 'New Book', 'author': self.author.id, 'publication_year': 2023}
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 2) # We are telling the program to check that no new book was created.

    # --- Test CRUD Operations (Authenticated) ---

    def test_create_book_authenticated(self):
        """
        We are testing that an authenticated user can create a new book.
        """
        self.client.force_authenticate(user=self.user)
        data = {'title': 'The Lord of the Rings', 'author': self.author.id, 'publication_year': 1954}
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3) # We are telling the program that a new book was successfully created.

    def test_update_book_authenticated(self):
        """
        We are testing that an authenticated user can update a book.
        """
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Harry Potter and the Sorcerer\'s Stone'}
        response = self.client.patch(f'/api/books/{self.book1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db() # We are telling the program to reload the book data from the database.
        self.assertEqual(self.book1.title, 'Harry Potter and the Sorcerer\'s Stone')

    def test_delete_book_authenticated(self):
        """
        We are testing that an authenticated user can delete a book.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # We are telling the program to check that the book is no longer in the database.
        self.assertEqual(Book.objects.count(), 1)

    # --- Test Filtering, Searching, and Ordering ---

    def test_search_books_by_title(self):
        """
        We are testing the search functionality on the 'title' field.
        """
        response = self.client.get('/api/books/?search=Philosopher')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book1.title)

    def test_search_books_by_author_name(self):
        """
        We are testing the search functionality on the 'author__name' field.
        """
        response = self.client.get('/api/books/?search=Rowling')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_publication_year(self):
        """
        We are testing the ordering functionality on the 'publication_year' field.
        """
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # We are telling the program to check if the first book is the oldest one.
        self.assertEqual(response.data[0]['title'], self.book1.title) 
        self.assertEqual(response.data[1]['title'], self.book2.title)
