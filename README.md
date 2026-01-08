# Post Management API: Secure Social Data Orchestration

The **Post Management API** is a high-performance, production-ready RESTful service designed for social media data management. Built with the **FastAPI** framework, this project serves as a comprehensive demonstration of modern backend engineering, including asynchronous programming, complex relational database logic, and high-entropy cryptographic security.

---

## 🏗️ Core Engineering Principles

The architecture of this application is founded on four pillars of modern software engineering: type safety, stateless security, persistent versioning, and environment parity.



### 1. High-Performance Asynchronous Design
The system is built using an **Asynchronous Server Gateway Interface (ASGI)** pattern. By leveraging Python's `asyncio` through the **Uvicorn** server, the API handles high-concurrency workloads without blocking execution threads. 

* **Data Validation**: Utilizing **Pydantic**, the API enforces strict data validation. Every request is checked against a schema before processing, ensuring that application logic never receives malformed data.
* **Serialization**: The system automatically handles conversion between complex database models (including joined vote counts) and JSON responses.

### 2. Advanced Security and Identity Management
Security is integrated at the core of the application through a multi-layered approach:

* **Argon2 Cryptographic Hashing**: User privacy is protected using the **Argon2** hashing algorithm via `passlib`. Argon2 is the winner of the Password Hashing Competition and provides superior resistance against GPU-based cracking compared to traditional algorithms.
* **Stateless Authentication**: The system utilizes **JSON Web Tokens (JWT)**. This allows the server to remain stateless, making it easier to scale across multiple cloud instances.
* **Authorization Scoping**: Every data request is subject to a strict ownership check. The API verifies the user's ID against the resource's `owner_id` within the database query itself.

### 3. Database Evolution and Relational Logic
The application utilizes **SQLAlchemy** as an Object-Relational Mapper (ORM) to interact with a **PostgreSQL** database.



* **Voting Logic**: The schema implements a Many-to-Many relationship simulation through a `votes` composite key table. The API logic handles "upvoting" and "downvoting" while preventing duplicate entries.
* **Schema Versioning**: To manage database changes, **Alembic** is used for migration tracking. This allows for incremental updates—such as adding the `votes` table—without risking data loss.
* **Referential Integrity**: The schema uses `ON DELETE CASCADE` logic. If a user deletes their account, the system automatically purges all associated posts and votes.

---

## 📂 Project Structure

```text
post-management-api/
├── alembic/                # Database migration history and env.py configuration
├── app/
│   ├── routers/            # Modular controllers: auth.py, user.py, post.py, vote.py
│   ├── config.py           # Pydantic-Settings for environment security
│   ├── database.py         # SQLAlchemy engine & session dependency setup
│   ├── main.py             # FastAPI entry point & CORS configuration
│   ├── models.py           # SQLAlchemy relational table definitions
│   ├── oauth2.py           # JWT generation and token verification logic
│   ├── schemas.py          # Pydantic validation & serialization models
│   └── utils.py            # Argon2 password hashing utility
├── alembic.ini             # Alembic configuration file
├── Procfile                # Deployment instructions for cloud platforms
├── requirements.txt        # Managed dependency manifest
└── .env                    # Environment secrets (ignored by Git)
🛠️ Tool Documentation and Usage
1. Authentication and User Management
User Registration: Access the /users endpoint to create a new account. Passwords are automatically hashed using Argon2 before storage.

JWT Login: Submit credentials to the /login endpoint to receive a Bearer Token. This token must be included in the Authorization header for all protected routes.

2. Post Orchestration and Interaction
CRUD Operations: Complete Create, Read, Update, and Delete capabilities for posts.

Voting System: Use the /vote endpoint to interact with content.

dir=1: Adds a vote to a post.

dir=0: Removes a previously cast vote.

⚙️ Installation and Setup
* Prerequisites
Python 3.11+

PostgreSQL Database

Virtual Environment (venv)

* Local Setup
Clone the Repository:

Bash

git clone [https://github.com/khallaftaha-cmyk/Post_Management_API](https://github.com/khallaftaha-cmyk/Post_Management_API)
cd Post_Management_API
Create and Activate Virtual Environment:

Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

Bash

pip install -r requirements.txt
Environment Configuration: Create a .env file in the root directory and fill in your credentials:

Extrait de code

DATABASE_HOSTNAME=your_host
DATABASE_PORT=5432
DATABASE_PASSWORD=your_password
DATABASE_NAME=your_db_name
DATABASE_USERNAME=your_user
SECRET_KEY=your_generated_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
Run Database Migrations:

Bash

alembic upgrade head
Start the Application:

Bash

uvicorn app.main:app --reload
* Interactive Documentation
Once the server is running, the API becomes self-documenting via OpenAPI:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

👨‍💻 Author Information
Taha Khallaf DevOps Engineer & Backend Developer

This project was developed to showcase full-stack backend mastery, from complex relational database design and managed migrations to high-entropy security and scalable API routing. If this infrastructure helps your workflow, please consider giving the repository a star!
