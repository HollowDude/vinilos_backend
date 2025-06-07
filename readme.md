# 🎵 VinyloStudios Backend — Django REST Framework

[View API Docs](https://github.com/tuusuario/vinilostudios-backend#readme)

## 📌 Description

This project is **the backend for VinyloStudios**, a platform for managing vinyl record collections, artists, and orders. Built with **Django REST Framework**, it exposes a clean, RESTful API that handles everything from user authentication to inventory and order processing.

No frontend included—just a rock-solid, API-first backend ready to be consumed by any client.

## 🛠️ Technologies

* **Python 3**
* **Django**
* **Django REST Framework**
* **PostgreSQL**
* **djangorestframework-simplejwt** (JWT authentication)
* **django-filter** (advanced filtering)

👉 Check out the code here:
[🔗 github.com/tuusuario/vinilostudios-backend](https://github.com/tuusuario/vinilostudios-backend)

## 🎨 Why Is It Interesting?

It illustrates how to build a **full-featured, production-grade API** with DRF, including:

* ViewSets & Routers for resourceful endpoints
* JWT-based auth flows (login, refresh, revoke)
* Nested serializers for artists → records
* Filter, search & pagination out of the box

Perfect as a boilerplate for any CRUD-heavy project or as a learning guide for DRF best practices.

---

## 🚀 How to Run It

1. **Clone the repo**

   ```bash
   git clone https://github.com/tuusuario/vinilostudios-backend.git
   cd vinilostudios-backend
   ```

2. **Create & activate a virtualenv**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your `.env`**

   ```env
   DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DBNAME
   SECRET_KEY=your-django-secret-key
   ```

5. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Explore the API**
   Visit [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) for browsable docs.

---

## 📣 Note

This API is deployed on **Render.com** at:
👉 [https://vinilostudios-backend.onrender.com/api/](https://vinilostudios-backend.onrender.com/api/)

---

## 📌 Author

Developed by **HollowDude**.
Contributions, issues and feedback are welcome—feel free to fork or open an issue!
