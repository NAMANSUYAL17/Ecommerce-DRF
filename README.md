# Django DRF E-Commerce Application

A full-stack e-commerce web application built with **Django**, **Django REST Framework (DRF)**, and **HTML/CSS/JavaScript**.  
This project demonstrates **user authentication**, **product listing**, **cart management**, and **secure API integration**.

---

## Features

- **User Authentication**
  - Registration and login using Django
  - JWT-based authentication for API endpoints
  - Authenticated users can add items to cart

- **Product Management**
  - CRUD operations via Django Admin
  - Product images handled using Django media
  - Product listing with pagination (Load More)

- **Cart System**
  - Add, update, remove items from cart
  - Cart actions protected for authenticated users
  - Redirects to login if unauthenticated

- **Frontend**
  - Server-rendered pages using HTML/CSS
  - Dynamic product loading via Fetch API
  - Navbar with login, register, and cart status

- **API**
  - RESTful endpoints for products, cart, and authentication
  - JWT token authentication
  - Paginated product list

---

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (can be switched to PostgreSQL)
- **Authentication:** JWT (SimpleJWT)
- **Version Control:** Git, GitHub
