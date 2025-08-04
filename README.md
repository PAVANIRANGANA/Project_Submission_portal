# 📂 PortalApp – Project Submission System

`PortalApp` is a core component of the **Project Submission Portal**, designed to streamline the process of students submitting academic or professional projects through a structured and user-friendly interface.

This app handles student submissions, project tracking, file uploads, and admin approvals — all through a web portal.

---

## 🚀 Features

- 📥 Student login and secure project submission
- 📄 Upload and manage project documents
- ✅ Admin panel for reviewing and approving submissions
- 📊 Dashboard to track submission status
- 📁 Organized storage for student-uploaded files
- 📨 Notifications or status updates (if implemented)

---

## 🛠️ Tech Stack

- **Backend**: Django / Flask (confirm yours)
- **Frontend**: HTML, CSS (Bootstrap / Tailwind if used)
- **Database**: SQLite / PostgreSQL / MySQL
- **Language**: Python 3.x

---

## 📁 Folder Structure
PortalApp/
├── init.py
├── models.py
├── views.py
├── forms.py
├── urls.py
├── templates/
│ └── submission_form.html
│ └── dashboard.html
├── static/
│ └── css/
│ └── js/
├── admin.py
├── apps.py
└── migrations/


---

## 🔧 Setup Instructions

1.**Clone the repo**:

git clone https://github.com/PAVANIRANGANA/Project_Submission_portal.git
cd Project_Submission_portal/ProjectPortal

2.**Set up a virtual environment**:

python -m venv venv
venv\Scripts\activate  # For Windows

or

source venv/bin/activate  # For Mac/Linux

3.**Install dependencies**:

pip install -r requirements.txt

4.**Apply migrations**:

python manage.py makemigrations
python manage.py migrate

5.**Run the server**:

python manage.py runserver

---

## 🙋‍♂️ Usage
Visit http://localhost:8000/

Students can submit projects through the form

Admins can log in to review submissions (superuser required)

Track submission statuses on the dashboard
