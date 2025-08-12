Filtering, Searching, and Ordering
The ListView for the book API has been configured to allow users to search, order, and filter the book list directly from the URL. This functionality is enabled by the filter_backends, search_fields, and ordering_fields attributes in the view.

Search Functionality
Implementation: The filters.SearchFilter has been enabled, allowing clients to search for text.

Fields: The search_fields attribute is set to ['title', 'author__name']. This tells the program to search for a query in both the book's title and the name of the author.

Example Usage: To find books containing the word "Python" in the title or by an author named "Python," use the query: /api/books/?search=Python

Ordering Functionality
Implementation: The filters.OrderingFilter has been enabled to control the order of results.

Fields: The ordering_fields attribute is set to ['title', 'publication_year']. This allows users to sort the list by either of these two fields.

Example Usage:

To sort books alphabetically by title: /api/books/?ordering=title

To sort books from newest to oldest: /api/books/?ordering=-publication_year
