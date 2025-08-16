# 📂 Project Submission Portal

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

A comprehensive web application built with Django, designed to streamline project submissions and reviews for students and administrators.

## 📑 Table of Contents
- [📂 Project Submission Portal](#-project-submission-portal)
- [🚀 Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🔧 Installation](#-installation)
- [🙋‍♂️ Usage](#‍♂️-usage)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🔗 Important links](#-important-links)
- [📄 Credits](#-credits)

---

## 🚀 Features

- 📥 **Student Project Submissions**: Streamlined project submissions via a user-friendly web interface.
- 📁 **Document Management**: Secure uploading and management of project-related documents.
- ✅ **Admin Review Panel**: Centralized admin interface for efficient project review and approval.
- 📊 **Status Tracking**: Real-time tracking of submission statuses for both students and admins.
- 🔐 **Secure Authentication**: Separate authentication flows for students and administrators.
- 📧 **Email Notifications**: Automated email notifications for submission status updates and feedback.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python Framework)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (Development) / PostgreSQL / MySQL (Production)
- **Language**: Python

---

## 🔧 Installation

1.  **Clone the repository**: 
    ```bash
    git clone https://github.com/PAVANIRANGANA/Project_Submission_portal.git
    ```
2.  **Navigate to the project directory**: 
    ```bash
    cd Project_Submission_portal/ProjectPortal
    ```
3.  **Set up a virtual environment**: 
    ```bash
    python -m venv venv
    ```
4.  **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
5.  **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
6.  **Apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
7.  **Run the development server**:
    ```bash
    python manage.py runserver
    ```

---

## 🙋‍♂️ Usage

- Visit `http://localhost:8000/` to access the portal.
- Students can register and submit projects through the web form.
- Administrators can log in to review and manage project submissions.
- Track submission statuses on the dashboard.

### Real-world use cases
* Streamlining academic project submissions
* Centralizing professional project reviews
* Managing document workflows

---

## 📁 Project Structure

```
ProjectPortal/
├── PortalApp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates/
│   │   ├── admin_view.html
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── home.html
│   │   ├── registration/
│   │   │   ├── dual_login.html
│   │   │   └── register.html
│   │   ├── review.html
│   │   └── submit_project.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── ProjectPortal/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── venv/
```

---

## 🤝 Contributing

Contributions are always welcome!

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes.
4.  Push to your fork.
5.  Submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🔗 Important links

*   Repository: [Project Submission portal](https://github.com/PAVANIRANGANA/Project_Submission_portal)
*   Author: [PAVANIRANGANA](https://github.com/PAVANIRANGANA)

---

## 📄 Credits

Developed by PAVANIRANGANA.

---

<p align=
