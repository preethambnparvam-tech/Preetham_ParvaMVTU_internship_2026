"""
Smart College ERP - Email Notifications Utility
Uses Django's built-in email backend (configure SMTP in settings.py)

Usage:
    from college_erp.email_utils import send_welcome_email, send_fee_reminder
"""

from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_welcome_email(student):
    """Send welcome email to newly registered student."""
    subject = f'Welcome to {settings.SITE_NAME if hasattr(settings, "SITE_NAME") else "Smart College ERP"}'
    message = f"""
Dear {student.get_full_name()},

Welcome to the Smart College ERP System!

Your login credentials:
  Username: {student.roll_number}
  Password: {student.roll_number}  (Please change after first login)

You can access the portal at: http://your-college-erp.com

Regards,
Administration Team
    """.strip()
    _send(subject, message, [student.email])


def send_fee_reminder(fee_record):
    """Send fee due reminder to student."""
    student = fee_record.student
    subject = f'Fee Payment Reminder - Due {fee_record.due_date}'
    message = f"""
Dear {student.get_full_name()},

This is a reminder that your fee payment is due soon.

  Description : {fee_record.description}
  Amount Due  : ₹{fee_record.balance}
  Due Date    : {fee_record.due_date}

Please make the payment before the due date to avoid a late fee.

Log in to pay: http://your-college-erp.com/fees/

Regards,
Accounts Department
    """.strip()
    _send(subject, message, [student.email])


def send_fee_receipt(fee_record):
    """Send payment confirmation to student."""
    student = fee_record.student
    subject = f'Payment Confirmed - Receipt #{fee_record.receipt_number}'
    message = f"""
Dear {student.get_full_name()},

Your payment has been received successfully.

  Receipt No : {fee_record.receipt_number}
  Description: {fee_record.description}
  Amount Paid: ₹{fee_record.amount_paid}
  Date       : {fee_record.paid_date}
  Method     : {fee_record.get_payment_method_display()}

Download your receipt from the ERP portal.

Regards,
Accounts Department
    """.strip()
    _send(subject, message, [student.email])


def send_low_attendance_alert(student, course, percentage):
    """Alert student and parent about low attendance."""
    subject = f'Attendance Warning - {course.name}'
    message = f"""
Dear {student.get_full_name()},

Your attendance in {course.name} ({course.code}) has fallen to {percentage:.1f}%.

The minimum required attendance is 75%. Students below this threshold
may not be permitted to sit for examinations.

Please regularize your attendance immediately.

Regards,
Academic Office
    """.strip()
    recipients = [student.email]
    if student.parent_name and '@' in (student.email or ''):
        pass  # Add parent email if stored
    _send(subject, message, recipients)


def send_bulk_fee_reminders():
    """Send reminders to all students with pending/overdue fees."""
    from fees.models import FeeRecord
    import datetime

    overdue = FeeRecord.objects.filter(
        status__in=['pending', 'overdue'],
        due_date__lte=datetime.date.today()
    ).select_related('student')

    messages = []
    for record in overdue:
        record.status = 'overdue'
        record.save()
        subject = f'[OVERDUE] Fee Payment - {record.description}'
        body = f'Dear {record.student.get_full_name()}, your fee of ₹{record.balance} is overdue. Please pay immediately.'
        messages.append((subject, body, settings.DEFAULT_FROM_EMAIL, [record.student.email]))

    if messages:
        send_mass_mail(messages, fail_silently=True)

    return len(messages)


def _send(subject, message, recipients):
    """Internal helper to send an email safely."""
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipients,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f'[Email Error] {e}')
        return False
