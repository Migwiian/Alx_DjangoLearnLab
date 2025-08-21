# Social Media API - User Authentication and Follow System

This Django REST Framework (DRF) project is the backend for a Social Media API. This current module handles user registration, login, and token-based authentication, along with the ability for users to follow and unfollow each other.

## 🚀 Features Implemented

- **Custom User Model**: Extended Django's default user model to include `bio`, `profile_picture`, and `followers`/`following` fields.
- **Token Authentication**: Secure user authentication using DRF's authtoken system.
- **Follow/Unfollow Functionality**: Users can create and delete follow relationships.
- **API Endpoints**:
  - `POST /api/auth/register/`: Register a new user.
  - `POST /api/auth/login/`: Log in an existing user and receive an authentication token.
  - `GET /api/auth/profile/`: Retrieve the profile of the currently authenticated user.
  - `POST /api/auth/follow/{username}/`: Follow a specific user.
  - `POST /api/auth/unfollow/{username}/`: Unfollow a specific user.

## 🛠️ Technology Stack

- **Python 3.12**
- **Django 4.2+**
- **Django REST Framework (DRF)**
- **SQLite** (Development Database)

## 📁 Project Structure
