CitySamadhan - Complaint Management System for Citizen
CitySamadhan is a web-based Complaint Management System for Citizen built to bridge the gap between citizens and civic authorities. Empowering citizens to resolve civic issues efficiently and transparently. It enables users to report, track, and discuss civic issues in their cities while providing departments with tools to address complaints effectively. Developed roject leverages modern web technologies to create a scalable, user-friendly solution for urban governance.

# 🏙️ CitySamadhan

> A Python-based centralized civic complaint management platform that enables citizens to report, track, and monitor public issues while helping municipal authorities resolve complaints efficiently.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-336791)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

CitySamadhan is a web-based civic issue reporting platform developed to bridge the communication gap between citizens and local authorities.

Users can report civic issues such as:

- 🗑️ Garbage Collection
- 🚧 Road Damage
- 💡 Street Light Failure
- 🚰 Water Leakage
- ⚡ Electricity Issues
- 🏢 Public Infrastructure Problems

Authorities receive, manage, assign, and update complaints through an administrative dashboard, ensuring transparency throughout the complaint lifecycle.

---

## ✨ Features

### 👤 User Features

- User Registration & Login
- Secure Authentication
- Submit Complaints
- Upload Complaint Images
- Location-based Complaint Reporting
- Track Complaint Status
- View Complaint History
- Upvote/Downvote Complaints
- Receive Notifications
- Responsive Dashboard

### 🛠️ Admin Features

- View All Complaints
- Assign Departments
- Update Complaint Status
- Manage Users
- Monitor Complaint Trends
- Notification Management

---

## 🚀 Tech Stack

### Backend

- Python
- Flask
- SQLAlchemy
- Flask-Mail
- GeoPy

### Frontend

- HTML5
- CSS3
- JavaScript

### Database

- SQLite (Development)
- PostgreSQL (Production)

### Tools

- VS Code
- Git & GitHub

---

## 🏗️ System Architecture

```
          User
            │
            ▼
      Flask Backend
            │
     Business Logic
            │
            ▼
     SQLAlchemy ORM
            │
            ▼
   SQLite / PostgreSQL
```

---

## 📂 Project Structure

```text
CitySamadhan/
│
├── app.py
├── models.py
├── routes.py
├── config.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── complaints.html
│   └── notifications.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
├── database/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/CitySamadhan.git
```

```bash
cd CitySamadhan
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Database

```bash
flask db upgrade
```

or

```bash
python app.py
```

### Start Server

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Registration

_Add Screenshot_

### Login

_Add Screenshot_

### Dashboard

_Add Screenshot_

### Submit Complaint

_Add Screenshot_

### Complaint Details

_Add Screenshot_

### Notifications

_Add Screenshot_

---

## 🗄️ Database Entities

- User
- Complaint
- Department
- Admin
- Notification

---

## 🔄 Workflow

1. User Registration
2. Login
3. Submit Complaint
4. Upload Image
5. Location Detection
6. Complaint Stored
7. Department Assignment
8. Status Updates
9. Notifications
10. Complaint Resolution

---

## 🧪 Testing

✔ User Registration

✔ Login Authentication

✔ Complaint Submission

✔ Complaint Tracking

✔ Status Update

✔ Notification System

✔ Database Integration

---

## 🔒 Security

- Password Authentication
- Session Management
- Input Validation
- Duplicate Account Prevention
- Secure Database Access

---

## 📈 Future Enhancements

- Mobile Application
- AI Complaint Classification
- Real-time Complaint Heatmaps
- GIS Integration
- SMS Notifications
- WhatsApp Notifications
- ML-based Priority Detection
- Analytics Dashboard
- Government API Integration

---

## 👨‍💻 Team

- Amit Kumar
- Akshita
- Ansh Mittal
- Gaurav Jangid

---

## 📚 Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite
- PostgreSQL
- HTML
- CSS
- JavaScript
- GeoPy
- Flask-Mail

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## ⭐ Show Your Support

If you like this project, please consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the MIT License.
