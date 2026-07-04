# 📝 Python Todo App

A simple full-stack Todo application built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **NiceGUI**.

This project was created to learn Python backend development after working with Node.js.

---

## 🚀 Features

- ✅ Create Todo
- 📋 View All Todos
- ✏️ Edit Todo
- ✔️ Mark Todo as Complete
- 🗑️ Delete Todo
- 🗄️ PostgreSQL Database
- 🎨 NiceGUI Frontend
- ⚡ FastAPI Backend
- 🔄 REST API

---

## 🛠️ Tech Stack

### Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

### Frontend

- NiceGUI

### Database

- PostgreSQL

---

## 📂 Project Structure

```
python_todo_app/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schema.py
│   ├── database.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── main.py
│   ├── component/
│   ├── services/
│   └── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/python-todo-app.git

cd python-todo-app
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure PostgreSQL

Create a database

```
todo_list
```

Update your database URL inside

```
database.py
```

Example

```python
DATABASE_URL = "postgresql+psycopg://postgres:password@localhost:5432/todo_list"
```

---

## ▶️ Run Backend

```bash
python -m uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Frontend

```bash
python main.py
```

NiceGUI will open

```
http://127.0.0.1:8080
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Home |
| POST | `/add_todo` | Create Todo |
| GET | `/all_todo` | Get All Todos |
| GET | `/get_todo_by_id/{id}` | Get Todo By ID |
| PUT | `/update_todo/{id}` | Update Todo |
| PUT | `/complete/{id}` | Complete Todo |
| DELETE | `/delete_todo/{id}` | Delete Todo |

---

# 📷 Screenshots

Add screenshots here.

Example

```
screenshots/
    home.png
    edit.png
```

---

# 🎯 Future Improvements

- 🔐 User Authentication
- 🌙 Dark Mode
- 📱 Responsive UI
- 🔍 Search Todos
- 🏷️ Todo Categories
- ⏰ Due Dates
- ⭐ Priority Levels
- 👥 Multi-user Support
- ☁️ Deploy on Render/Railway

---

# 📖 What I Learned

- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- REST APIs
- NiceGUI
- CRUD Operations
- Python Project Structure
- Virtual Environments
- API Integration

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the project
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Neeraj Dhyani**

GitHub: https://github.com/Neeraj-Dhyani

---

⭐ If you like this project, give it a star on GitHub!
