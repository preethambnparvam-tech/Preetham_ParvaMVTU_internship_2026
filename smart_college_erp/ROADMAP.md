# 🗺️ Smart College ERP — Development Roadmap

> ParvaM Consul-tech Pvt. Ltd. | Capstone Internship Project
> This roadmap covers Phase 1 (MVP), Phase 2 (Advanced), and Phase 3 (Production-Ready).

---

## ✅ Phase 1 — Core MVP (Weeks 1–4)

> Goal: Working ERP with all 5 modules and role-based login.

### Week 1 — Project Setup & Authentication

- [x] Django project scaffold (`college_erp`)
- [x] 5 apps created: `students`, `faculty`, `attendance`, `fees`, `timetable`
- [x] Bootstrap 5 base template with sidebar layout
- [x] Login / Logout views
- [x] Role-based groups: Admin, HOD, Faculty, Student
- [x] `setup_erp` management command (auto-creates groups, admin, departments)
- [x] UUID primary keys on all models
- [x] `manage.py` + `wsgi.py` + `requirements.txt`

### Week 2 — Student & Faculty Modules

- [x] Department model (code, name, HOD)
- [x] Course model (code, name, department, semester, credits, faculty)
- [x] Student model (full profile, photo, parent info)
- [x] Student CRUD (list, add, edit, soft-delete)
- [x] Student search + filter (name, roll no, dept, sem)
- [x] Paginated student list (20 per page)
- [x] Auto-creates Django auth user on student add
- [x] Faculty model (employee ID, designation, specialization)
- [x] Faculty CRUD (list, add, edit, deactivate)
- [x] Faculty linked to courses

### Week 3 — Attendance & Timetable

- [x] `AttendanceSession` model (course, faculty, date, QR token)
- [x] `AttendanceRecord` model (student, course, date, status)
- [x] `AttendanceSummary` model (precomputed percentage)
- [x] Session creation with QR code auto-generation
- [x] Bulk attendance marking (present/absent/late/excused)
- [x] QR scan view (students auto-mark via phone)
- [x] Attendance percentage report (flagged < 75%)
- [x] `TimeSlot` + `Timetable` models
- [x] Weekly timetable grid view
- [x] Timetable entry add/remove

### Week 4 — Fee Management & Exports

- [x] `FeeStructure` model (per dept/semester/academic year)
- [x] `FeeRecord` model (per student, payment tracking)
- [x] Fee dashboard (collected / pending / overdue stats)
- [x] Record payments (Cash, UPI, NEFT, DD, Card)
- [x] Auto receipt number generation on payment
- [x] CSV export: Students, Faculty, Attendance, Fees
- [x] PDF export: Student list report (WeasyPrint)
- [x] PDF fee receipt per payment
- [x] Email notification: fee confirmation
- [x] Email utility module (`email_utils.py`)

---

## 🔄 Phase 2 — Advanced Features (Weeks 5–8)

> Goal: Enhance UX, add automation, real-time features.

### Week 5 — Role-Based Access Control (RBAC)

- [ ] Django `@permission_required` decorators on all views
- [ ] Custom middleware to restrict access by role
- [ ] HOD dashboard: own department overview only
- [ ] Faculty dashboard: own sessions, own courses
- [ ] Student dashboard: own profile, own attendance, own fees
- [ ] Admin: full access
- [ ] Redirect unauthorized users gracefully

### Week 6 — PDF & Excel Enhancements

- [ ] Attendance report PDF (per student, per course, date-range filter)
- [ ] Fee collection report PDF (by month / department / status)
- [ ] `.xlsx` export using `openpyxl` (formatted with colors/borders)
- [ ] Timetable PDF export per department
- [ ] Student ID card PDF generation (with photo + QR code)
- [ ] Bulk PDF generation (all fee receipts for a semester)

### Week 7 — Notifications & Automation

- [ ] Automated weekly email: fee reminders for pending records
- [ ] Automated monthly: attendance summary email to students & parents
- [ ] Django management command: `send_fee_reminders`
- [ ] Django management command: `flag_overdue_fees`
- [ ] Django management command: `send_attendance_alerts`
- [ ] Django Signals: auto-send welcome email on student creation
- [ ] In-app notification bell (unread count, dismiss)
- [ ] SMS gateway integration (Twilio / MSG91) — optional

### Week 8 — Advanced Attendance

- [ ] Geo-location check on QR scan (validate student is on campus)
- [ ] QR code expiry timer (auto-deactivate after N minutes)
- [ ] Face recognition attendance — optional ML integration
- [ ] Bulk attendance import via CSV upload
- [ ] Attendance regularization request (student → faculty approval)
- [ ] Leave management (student applies, faculty/HOD approves)
- [ ] Calendar view of attendance per student

---

## 🚀 Phase 3 — Production Ready (Weeks 9–12)

> Goal: Deployment, security, scalability, API.

### Week 9 — REST API (Django REST Framework)

- [ ] Install and configure DRF
- [ ] Student API endpoints (list, detail, create, update)
- [ ] Faculty API endpoints
- [ ] Attendance API (mark, fetch summary)
- [ ] Fee API (list, pay)
- [ ] JWT authentication (`djangorestframework-simplejwt`)
- [ ] API documentation (Swagger via `drf-yasg` or `drf-spectacular`)
- [ ] Rate limiting on API endpoints

### Week 10 — UI & UX Improvements

- [ ] Fully responsive mobile layout (tested on phones/tablets)
- [ ] Dark mode toggle (CSS variables based)
- [ ] DataTables integration (client-side sort/search/paginate)
- [ ] Chart.js dashboard charts (attendance trends, fee collection)
- [ ] Drag-and-drop timetable builder
- [ ] Student photo upload preview + crop
- [ ] Skeleton loading screens
- [ ] Toast notifications (real-time feedback)

### Week 11 — Security & Testing

- [ ] Move `SECRET_KEY` and DB credentials to `.env` (python-decouple)
- [ ] `DEBUG=False` in production with `ALLOWED_HOSTS` set
- [ ] HTTPS enforcement (`SECURE_SSL_REDIRECT`, HSTS headers)
- [ ] CSRF protection verified across all forms
- [ ] SQL injection audit (Django ORM protects by default)
- [ ] File upload validation (size, type, malware scan)
- [ ] Unit tests for all model methods
- [ ] Integration tests for all CRUD views
- [ ] Selenium tests for critical user flows (login, attendance mark, fee pay)
- [ ] Code coverage report (`coverage.py`)

### Week 12 — Deployment

- [ ] Switch to PostgreSQL (`psycopg2-binary`)
- [ ] Serve static/media via WhiteNoise or AWS S3
- [ ] Configure Gunicorn + Nginx
- [ ] Docker + `docker-compose.yml` setup
- [ ] CI/CD pipeline (GitHub Actions):
  - Lint (flake8)
  - Test (pytest)
  - Build Docker image
  - Deploy to server
- [ ] Environment variable management in production
- [ ] Database backups (cron + pg_dump)
- [ ] Health check endpoint `/health/`
- [ ] Error monitoring (Sentry)
- [ ] Deploy to VPS / Heroku / Railway / Render

---

## 🌟 Future Enhancements (Post-Internship)

| Feature | Description |
|---|---|
| **Mobile App** | React Native app for students (attendance, fees, timetable) |
| **Exam Management** | Exam schedule, hall tickets, result entry |
| **Library Module** | Book inventory, issue/return, fine management |
| **Hostel Module** | Room allocation, warden dashboard |
| **Placement Module** | Company registration, student applications, interview scheduler |
| **Online Assignments** | Faculty upload, student submit, grading |
| **Live Chat** | Student ↔ Faculty messaging |
| **Analytics Dashboard** | Department-wise performance charts, trend analysis |
| **Multi-College** | Tenant-based architecture for college groups |
| **Biometric Integration** | Fingerprint/Face ID attendance hardware |

---

## 📊 Sprint Summary

| Sprint | Duration | Key Deliverable |
|---|---|---|
| Sprint 1 | Week 1 | Auth, project setup, groups |
| Sprint 2 | Week 2 | Students + Faculty modules |
| Sprint 3 | Week 3 | Attendance + Timetable |
| Sprint 4 | Week 4 | Fees + Exports + Email |
| Sprint 5 | Week 5 | RBAC enforcement |
| Sprint 6 | Week 6 | PDF/Excel enhancements |
| Sprint 7 | Week 7 | Notifications + automation |
| Sprint 8 | Week 8 | Advanced attendance |
| Sprint 9 | Week 9 | REST API |
| Sprint 10 | Week 10 | UI/UX polish |
| Sprint 11 | Week 11 | Security + Testing |
| Sprint 12 | Week 12 | Deployment & CI/CD |

---

## 🔧 Git Branching Strategy

```
main              ← Production-ready code only
  └── develop     ← Integration branch
        ├── feature/student-module
        ├── feature/attendance-qr
        ├── feature/fee-pdf-receipt
        ├── feature/rest-api
        └── hotfix/login-bug
```

**Commit convention:**
```
feat: add QR attendance generation
fix: correct attendance percentage calculation
docs: update README setup steps
style: format views.py with black
test: add unit tests for FeeRecord.balance
```

---

> 📅 Last Updated: 2025 | ParvaM Consul-tech Pvt. Ltd. | Bengaluru 560090
