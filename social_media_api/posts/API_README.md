Social Media API DocumentationThis document provides a comprehensive guide to the API endpoints for the social media platform, including user authentication, posts, and comments. All endpoints are accessible at the base URL: http://127.0.0.1:8000/.AuthenticationAll POST, PUT, PATCH, and DELETE requests require an authentication token. You can obtain a token by registering or logging in.Register a UserURL: /accounts/register/Method: POSTDescription: Creates a new user account and returns an authentication token.Request Body:{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "strong_password_123"
}

Response:{
    "username": "newuser",
    "email": "newuser@example.com",
    "token": "d748d56b0f14d9b23f2f0b9f564d6c7e2b14d87f"
}

Log In a UserURL: /accounts/login/Method: POSTDescription: Logs in an existing user and returns their authentication token.Request Body:{
    "username": "newuser",
    "password": "strong_password_123"
}

Response:{
    "username": "newuser",
    "email": "newuser@example.com",
    "token": "d748d56b0f14d9b23f2f0b9f564d6c7e2b14d87f"
}

PostsThese endpoints handle all operations related to posts. Authentication is required for all actions except GET list and detail.List All PostsURL: /api/posts/Method: GETDescription: Retrieves a paginated list of all posts.Query Parameters:?page_size=10: Sets the number of items per page.?search=query: Filters posts by title and content.Response:{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "newuser",
            "title": "Hello World",
            "content": "This is my first post!",
            "created_at": "2024-05-15T12:00:00Z",
            "updated_at": "2024-05-15T12:00:00Z",
            "comments": []
        }
    ]
}

Create a New PostURL: /api/posts/Method: POSTDescription: Creates a new post.Authentication: Required (via Authorization: Token <your_token>)Request Body:{
    "title": "My Post",
    "content": "This is the content of my new post."
}

Response:{
    "id": 2,
    "author": "newuser",
    "title": "My Post",
    "content": "This is the content of my new post.",
    "created_at": "2024-05-15T12:01:00Z",
    "updated_at": "2024-05-15T12:01:00Z",
    "comments": []
}

Retrieve a Single PostURL: /api/posts/{id}/Method: GETDescription: Retrieves a single post by its ID, including related comments.Response:{
    "id": 1,
    "author": "newuser",
    "title": "Hello World",
    "content": "This is my first post!",
    "created_at": "2024-05-15T12:00:00Z",
    "updated_at": "2024-05-15T12:00:00Z",
    "comments": [
        {
            "id": 1,
            "post": 1,
            "author": "anotheruser",
            "content": "Great post!",
            "created_at": "2024-05-15T12:05:00Z",
            "updated_at": "2024-05-15T12:05:00Z"
        }
    ]
}

Update a PostURL: /api/posts/{id}/Method: PATCH (for partial update) or PUT (for full update)Description: Updates an existing post.Authentication: Required, and you must be the author of the post.Request Body:{
    "content": "This is my updated content."
}

Response:{
    "id": 1,
    "author": "newuser",
    "title": "Hello World",
    "content": "This is my updated content.",
    "created_at": "2024-05-15T12:00:00Z",
    "updated_at": "2024-05-15T12:06:00Z",
    "comments": []
}

Delete a PostURL: /api/posts/{id}/Method: DELETEDescription: Deletes a post.Authentication: Required, and you must be the author of the post.Response: 204 No ContentCommentsThese endpoints handle all operations related to comments. Authentication is required for all actions except GET list and detail.List All CommentsURL: /api/comments/Method: GETDescription: Retrieves a paginated list of all comments.Response:{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "post": 1,
            "author": "testuser",
            "content": "Great post!",
            "created_at": "2024-05-15T12:05:00Z",
            "updated_at": "2024-05-15T12:05:00Z"
        }
    ]
}

Create a New CommentURL: /api/comments/Method: POSTDescription: Creates a new comment on a post.Authentication: Required.Request Body:{
    "post": 1,
    "content": "This is my comment!"
}

Response:{
    "id": 2,
    "post": 1,
    "author": "newuser",
    "content": "This is my comment!",
    "created_at": "2024-05-15T12:07:00Z",
    "updated_at": "2024-05-15T12:07:00Z"
}

Retrieve a Single CommentURL: /api/comments/{id}/Method: GETDescription: Retrieves a single comment by its ID.Response: (Same as a single item in the list response)Update a CommentURL: /api/comments/{id}/Method: PATCH or PUTDescription: Updates an existing comment.Authentication: Required, and you must be the author of the comment.Request Body:{
    "content": "My updated comment."
}

Response: (Same as a single item in the list response, with updated updated_at)Delete a CommentURL: /api/comments/{id}/Method: DELETEDescription: Deletes a comment.Authentication: Required, and you must be the author of the comment.Response: 204 No Content