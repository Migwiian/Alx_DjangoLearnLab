# API Testing Strategy

This document outlines the approach for testing the API endpoints.

## Test File
Unit tests are located in `api/test_views.py`.

## Key Areas Tested
* **CRUD Operations:** Verifies that books can be created, retrieved, updated, and deleted.
* **Permissions:** Ensures that `IsAuthenticatedOrReadOnly` and `IsAuthenticated` permissions are correctly enforced.
* **Filtering, Searching, & Ordering:** Confirms that the `ListView` correctly handles query parameters for searching and sorting.

## Running Tests
To run the test suite, navigate to the project's root directory and use the following command:
`python manage.py test api`
