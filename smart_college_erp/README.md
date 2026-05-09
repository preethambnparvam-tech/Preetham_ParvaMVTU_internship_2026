# 🎓 Smart College ERP System

> A full-featured Django Full Stack ERP built for educational institutions.
> Developed as a Capstone Internship Project — **ParvaM Consul-tech Pvt. Ltd., Bengaluru**

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Modules](#modules)
- [Roles & Permissions](#roles--permissions)
- [Advanced Features](#advanced-features)
- [Environment Variables](#environment-variables)
- [API Reference](#api-reference)
- [Contributing](#contributing)

---

## ✨ Features

| Module | Capabilities |
|---|---|
| **Student Management** | CRUD, profile photos, search/filter, paginated list, CSV + PDF export |
| **Faculty Management** | Employee profiles, designation, department assignment, course linking |
| **Attendance System** | Session-based, QR code generation & scanning, bulk marking, percentage report |
| **Fee Management** | Fee structures, payment tracking, PDF receipts, overdue detection, email alerts |
| **Timetable** | Visual weekly grid, time slots, room allocation, department/semester filter |

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.11+, Django 4.2 |
| **Database** | SQLite (dev) → PostgreSQL (prod) |
| **Frontend** | Bootstrap 5.3, Bootstrap Icons |
| **PDF Export** | WeasyPrint |
| **QR Codes** | qrcode + Pillow |
| **Email** | Django SMTP (Gmail / SendGrid) |
| **Excel Export** | Built-in CSV (openpyxl for xlsx) |

---

## 📁 Project Structure

```
smart_college_erp/
├── manage.py
├── requirements.txt
├── college_erp/              # Project config
│   ├── settings.py
│   ├── urls.py
│   ├── views.py              # Dashboard & home
│   ├── wsgi.py
│   └── email_utils.py        # Email notification helpers
│
├── students/                 # Student & Department & Course app
│   ├── models.py             # Student, Department, Course
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── management/commands/
│       └── setup_erp.py      # Initial data setup command
│
├── faculty/                  # Faculty app
│   ├── models.py             # Faculty
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── attendance/               # Attendance app
│   ├── models.py             # AttendanceSession, AttendanceRecord, AttendanceSummary
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templatetags/
│       └── erp_tags.py       # Custom template filters
│
├── fees/                     # Fee Management app
│   ├── models.py             # FeeStructure, FeeRecord
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── timetable/                # Timetable app
│   ├── models.py             # TimeSlot, Timetable
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   ├── base/
│   │   ├── base.html         # Sidebar layout
│   │   ├── login.html
│   │   └── dashboard.html
│   ├── students/
│   ├── faculty/
│   ├── attendance/
│   ├── fees/
│   └── timetable/
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
└── media/
    ├── students/photos/
    ├── faculty/photos/
    └── attendance/qr/
```

---

## 🚀 Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/your-org/smart-college-erp.git
cd smart_college_erp

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the project root:

```env
SECRET_KEY=your-very-secret-key-here
DEBUG=True
EMAIL_HOST_USER=yourmail@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 3. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Initial Setup (Groups + Admin + Sample Departments)

```bash
python manage.py setup_erp
# Default: admin / admin123
```

### 5. Run

```bash
python manage.py runserver
```

Visit → **http://127.0.0.1:8000/**

---

## 📦 Modules

### 🎓 Student Management
- Add / Edit / Deactivate students
- Profile photo upload
- Search by name, roll number, email
- Filter by department and semester
- View attendance & fee history per student
- Export to **CSV** (Excel-compatible)
- Export to **PDF** (requires WeasyPrint)

### 👩‍🏫 Faculty Management
- Full profile with designation, qualification, specialization
- Department assignment
- Linked course assignments
- Auto-creates Django user account (username = Employee ID)

### 📅 Attendance System
- **Sessions**: Faculty creates a session per class
- **QR Code**: Auto-generated QR; students scan to self-mark
- **Manual**: Bulk mark present/absent/late/excused per student
- **Summary**: Attendance % per student per course
- Low attendance alerts (< 75% flagged in reports)
- CSV export

### 💳 Fee Management
- Define **Fee Structures** per department/semester/year
- Create individual **Fee Records** per student
- Record payments (Cash, UPI, NEFT, DD, Card)
- **PDF Receipts** generated on payment (WeasyPrint)
- Email confirmation on payment
- Overdue auto-detection
- CSV export of all records

### 🗓 Timetable
- Visual weekly grid (days × time slots)
- Add time slots (e.g., 9:00–10:00)
- Assign course + faculty + room per slot
- Filter by department and semester

---

## 👥 Roles & Permissions

| Role | Access |
|---|---|
| **Admin / Superuser** | Full access to all modules + Django admin panel |
| **HOD** | View department students, faculty; approve leaves (extensible) |
| **Faculty** | Create attendance sessions, mark attendance, view reports |
| **Student** | View own profile, attendance summary, fee records; QR scan |

Roles are managed via **Django Groups**. Created automatically by `setup_erp`.

---

## 🔧 Advanced Features

### QR Code Attendance
1. Faculty creates an attendance session
2. A unique QR code is generated and saved
3. Faculty displays QR in class
4. Students scan with phone → attendance auto-marked as "Present"
5. Token expires when session is deactivated

Install: `pip install qrcode[pil]`

### PDF Reports
- Student list PDF (all active students)
- Fee receipt PDF per payment
- Uses **WeasyPrint**: `pip install weasyprint`

### Excel / CSV Export
- Students, Faculty, Attendance, Fees
- Built-in Python `csv` module — no extra install needed
- For `.xlsx` format: `pip install openpyxl`

### Email Notifications
Configured in `settings.py` (SMTP):
- Welcome email on student registration
- Fee payment confirmation with receipt details
- Fee due reminders
- Low attendance alerts

---

## ⚙️ Environment Variables

| Variable | Description | Default |
|---|---|---|
| `SECRET_KEY` | Django secret key | (set in settings) |
| `DEBUG` | Debug mode | `True` |
| `EMAIL_HOST_USER` | SMTP email address | `''` |
| `EMAIL_HOST_PASSWORD` | SMTP app password | `''` |
| `DB_NAME` | PostgreSQL DB name | — |
| `DB_USER` | PostgreSQL user | — |
| `DB_PASSWORD` | PostgreSQL password | — |
| `DB_HOST` | PostgreSQL host | `localhost` |

---

## 🧰 Useful Commands

```bash
# Create initial setup
python manage.py setup_erp

# Create migrations after model changes
python manage.py makemigrations
python manage.py migrate

# Create superuser manually
python manage.py createsuperuser

# Collect static files (production)
python manage.py collectstatic

# Send bulk fee reminders
python manage.py shell -c "from college_erp.email_utils import send_bulk_fee_reminders; send_bulk_fee_reminders()"

# Run tests
python manage.py test
```

---

## 🗃 Database Schema (Key Models)

```
Department ──< Course
Department ──< Student ──< AttendanceRecord
Department ──< Faculty ──< AttendanceSession
Student ──< FeeRecord >── FeeStructure
Course + Student ──< AttendanceSummary
Department + Semester + Day + TimeSlot ──< Timetable
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---|---|
| WeasyPrint install fails | Install system deps: `apt install libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0` |
| QR codes not generating | Run `pip install qrcode[pil] Pillow` |
| Email not sending | Check Gmail App Password in settings; use App-Specific Password |
| Static files not loading | Run `python manage.py collectstatic` |
| Timetable grid template error | Ensure `{% load erp_tags %}` is added if using custom filters |

---

## 📄 License

This project was created as a capstone internship project at **ParvaM Consul-tech Pvt. Ltd.**
For educational use. All rights reserved.

---

> Built with ❤️ using Django | Bootstrap 5 | ParvaM Consul-tech, Bengaluru 560090
