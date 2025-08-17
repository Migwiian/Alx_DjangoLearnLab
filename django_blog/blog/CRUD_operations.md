# Django Blog CRUD Project

This project expands on a basic Django blog application by implementing a complete **CRUD (Create, Read, Update, Delete)** system for blog posts. This allows authenticated users to dynamically manage their content.

## Features

### Blog Post Management
Users with an account can now fully interact with blog posts.

* **View Posts**: Browse a list of all blog posts on the home page. Click on a post title to see the full content.
* **Create Posts**: Authenticated users can write and publish new blog posts. The author is automatically set to the logged-in user.
* **Edit Posts**: Authors can modify the title and content of their own posts.
* **Delete Posts**: Authors have the ability to delete their own posts.

### Security and Permissions
Access to certain features is restricted to ensure content integrity and security.

* **Authentication**: Users must be logged in to create a new post.
* **Authorization**: Only the original author of a blog post can edit or delete it. Attempts by other users to access these functions are blocked.

---

## Technical Implementation

This project was built using Django's powerful class-based views to streamline development.

| Feature       | Django Class-Based View | Mixin(s) Used                             | URL                             |
| :------------ | :---------------------- | :---------------------------------------- | :------------------------------ |
| **View List** | `ListView`              | None                                      | `/posts/`                       |
| **View Detail** | `DetailView`            | None                                      | `/posts/<int:pk>/`              |
| **Create** | `CreateView`            | `LoginRequiredMixin`                      | `/posts/new/`                   |
| **Update** | `UpdateView`            | `LoginRequiredMixin`, `UserPassesTestMixin` | `/posts/<int:pk>/edit/`         |
| **Delete** | `DeleteView`            | `LoginRequiredMixin`, `UserPassesTestMixin` | `/posts/<int:pk>/delete/`       |

A `ModelForm` was used for the `Post` model to handle data validation and submission for the create and update views.

The `LoginRequiredMixin` ensures a user is logged in before accessing a view, while the `UserPassesTestMixin` provides the custom logic to verify that the requesting user is the same as the post's author. This is handled by the `test_func` method, which is implemented in both the `UpdatePostView` and `DeletePostView` classes.
