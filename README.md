# 💻 Full-Stack Django Web Application

A full-featured Django-based web platform that includes user authentication, project showcasing, messaging, commenting, and a REST API. Designed with modularity and scalability in mind.

---

## ✨ Features

- 🔐 **User Authentication**: Login, registration, and secure access control  
- 💬 **Messaging System**: Users can send and receive private messages  
- 📝 **Commenting**: Leave feedback or discuss under project listings  
- ⭐ **Project Rating**: Rate projects to reflect their usefulness or quality  
- 🔍 **Search & Pagination**: Easily find projects and browse with pagination  
- 🛠 **API Development**: RESTful APIs for external integrations  
- 🧱 **Class-Based Views**: Scalable and reusable view logic  
- 🧩 **Template Inheritance**: Clean and consistent UI using Django templating  
- 📦 **Static Files Management**: Easily manage CSS, JS, and media assets  
- 🎨 **Custom Themes**: Add or switch themes to personalize the design  

---

## 🗂 Technologies Used

- **Backend**: Django, Django REST Framework  
- **Frontend**: HTML5, CSS3, JavaScript  
- **Database**: SQLite (default), PostgreSQL (optional)  
- **Authentication**: Django’s built-in auth system  
- **Deployment**: (Optional) Ready for deployment on Render, Heroku, or AWS  

---

## 🛠 Core Concepts Practiced

- **CRUD Operations** – Create, Read, Update, Delete for project and user data  
- **Model Design** – Structured relational models for users, messages, and projects  
- **Routing & Views** – Clean URL routing with function/class-based views  
- **Reusable Templates** – DRY templating for consistent UI/UX  

---

## 🚀 Getting Started

1. Clone this repository  
2. Create a virtual environment and install requirements  
3. Run migrations and start the development server  

```bash
git clone <your-repo-url>
cd project-folder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
