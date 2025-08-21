# Social Media API - User Authentication Module

This Django REST Framework (DRF) project is the backend for a Social Media API. This module handles user registration, login, and token-based authentication.

## 🚀 Features Implemented

- **Custom User Model**: Extended Django's default user model to include `bio`, `profile_picture`, and `followers` fields.
- **Token Authentication**: Secure user authentication using DRF's authtoken system.
- **API Endpoints**:
  - `POST /api/auth/register/`: Register a new user.
  - `POST /api/auth/login/`: Log in an existing user and receive an authentication token.
  - `GET /api/auth/profile/`: (Protected) Retrieve the profile of the currently authenticated user.

