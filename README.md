# 🎓 Student Management System (Django)

A simple web app built with **Django** to add, view, search and delete student records. Data is stored in a SQLite database.

---

## 📌 Features

- ➕ Add a student (name, email, date of birth, mobile number)
- 📋 View all students
- 🔍 Search students by name
- 🗑️ Delete students (search by name, then delete)

---

## 🛠️ Tech Stack

| Part | Technology |
|------|-----------|
| Backend | Python, Django |
| Database | SQLite |
| Frontend | Django templates (HTML) |

---

## 📁 Project Structure

```
Student_Management_System_Django/
│
├── Student_Management_System/   # Django project (settings, urls)
├── Student_Details/             # App: models, views, urls
├── templates/                   # base, index, Add/Show/Find/Delete pages
└── manage.py
```

---

## 🔗 Pages

| URL | Description |
|-----|-------------|
| `/` | Home page |
| `/Add_Student/` | Add student form |
| `/Show_Student/` | List all students |
| `/Find_Student/?q=name` | Search students by name |
| `/Delete_Student/` | Find students by name and delete |

---

## ▶️ How to Run

```bash
git clone https://github.com/sumitkumar01104/Student_Management_System_Django.git
cd Student_Management_System_Django

python -m venv venv
venv\Scripts\activate           # Windows
source venv/bin/activate        # Linux/Mac

pip install django
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 📚 Learning Purpose
This project was created as part of my Django learning journey to practice models, views, templates and CRUD operations.

## 👨‍💻 Author
**Sumit Nagar**
📍 Uttar Pradesh, India

## 🤝 Connect with Me
- 💼 **GitHub**: [@sumitkumar01104](https://github.com/sumitkumar01104)
- 📸 **Instagram**: [@i..sumit..nagar](https://www.instagram.com/i._.sumit._.nagar?igsh=MW95OHE3aW1maWR3bQ==)
- 💬 **Telegram**: [@i_sumit_nagar](https://t.me/Sumitkumarha386)
