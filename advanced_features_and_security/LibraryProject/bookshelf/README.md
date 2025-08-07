Permissions and Groups Setup
This guide provides an overview of the user groups and permissions for the bookshelf application.

Defined Permissions:

1. can_create: Allows a user to add a new Book.

2. can_edit: Grants a user the ability to modify a book.

3. can_view: Allows a user to view books.

4. can_delete: Grants a user the ability to remove a book.

User Groups and Assigned Permissions:

1. Admins: Intended for users with full control. Permissions: can_create, can_edit, can_delete, can_view.

2. Editors: For users responsible for creating and updating content. Permissions: can_create, can_edit, can_view.

3. Viewers: For users who only need to browse the collection. Permissions: can_view.

Enforcing Permissions in Views:
Permissions are enforced using the @permission_required decorator in the views.py file. This decorator acts as a security check.

Example from views.py: @permission_required('bookshelf.can_edit', raise_exception=True) def edit_book(request, pk): ...
