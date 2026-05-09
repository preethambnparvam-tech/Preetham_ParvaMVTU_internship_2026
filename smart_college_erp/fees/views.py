"""
Fees App - Views
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Sum, Q
from django.template.loader import render_to_string

from .models import FeeRecord, FeeStructure
from students.models import Student, Department
from .forms import FeeRecordForm, FeeStructureForm


@login_required
def fee_dashboard(request):
    total_collected = FeeRecord.objects.filter(status='paid').aggregate(
        total=Sum('amount_paid')
    )['total'] or 0
    total_pending = FeeRecord.objects.filter(status__in=['pending', 'overdue']).aggregate(
        total=Sum('amount')
    )['total'] or 0
    overdue_count = FeeRecord.objects.filter(status='overdue').count()

    recent_payments = FeeRecord.objects.filter(status='paid').order_by('-paid_date')[:10]

    return render(request, 'fees/dashboard.html', {
        'total_collected': total_collected,
        'total_pending': total_pending,
        'overdue_count': overdue_count,
        'recent_payments': recent_payments,
    })


@login_required
def fee_list(request):
    records = FeeRecord.objects.select_related('student', 'student__department').all()
    status = request.GET.get('status', '')
    dept = request.GET.get('dept', '')
    q = request.GET.get('q', '')

    if status:
        records = records.filter(status=status)
    if dept:
        records = records.filter(student__department__id=dept)
    if q:
        records = records.filter(
            Q(student__roll_number__icontains=q) |
            Q(student__first_name__icontains=q) |
            Q(student__last_name__icontains=q)
        )

    return render(request, 'fees/fee_list.html', {
        'records': records,
        'departments': Department.objects.all(),
        'status': status, 'dept': dept, 'q': q,
        'status_choices': FeeRecord.STATUS_CHOICES,
    })


@login_required
def fee_create(request):
    if request.method == 'POST':
        form = FeeRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fee record created.')
            return redirect('fees:fee_list')
    else:
        form = FeeRecordForm()
    return render(request, 'fees/fee_form.html', {'form': form, 'title': 'Add Fee Record'})


@login_required
def fee_pay(request, pk):
    """Mark a fee as paid / partial."""
    record = get_object_or_404(FeeRecord, pk=pk)
    if request.method == 'POST':
        amount_paid = request.POST.get('amount_paid', 0)
        payment_method = request.POST.get('payment_method', '')
        transaction_id = request.POST.get('transaction_id', '')

        record.amount_paid = float(amount_paid)
        record.payment_method = payment_method
        record.transaction_id = transaction_id

        if record.amount_paid >= float(record.amount):
            record.status = 'paid'
        else:
            record.status = 'partial'

        import datetime
        record.paid_date = datetime.date.today()
        record.save()

        # Send email notification
        try:
            _send_fee_receipt_email(record)
        except Exception:
            pass

        messages.success(request, f'Payment of ₹{record.amount_paid} recorded.')
        return redirect('fees:fee_detail', pk=pk)

    return render(request, 'fees/fee_pay.html', {
        'record': record,
        'payment_methods': FeeRecord.PAYMENT_METHODS,
    })


@login_required
def fee_detail(request, pk):
    record = get_object_or_404(FeeRecord, pk=pk)
    return render(request, 'fees/fee_detail.html', {'record': record})


@login_required
def fee_receipt_pdf(request, pk):
    """Generate PDF receipt for a paid fee."""
    record = get_object_or_404(FeeRecord, pk=pk)
    try:
        from weasyprint import HTML
        html_string = render_to_string('fees/receipt_pdf.html', {'record': record})
        html = HTML(string=html_string)
        pdf = html.write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="receipt_{record.receipt_number}.pdf"'
        return response
    except ImportError:
        messages.error(request, 'WeasyPrint not installed. Run: pip install weasyprint')
        return redirect('fees:fee_detail', pk=pk)


@login_required
def export_fees_csv(request):
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fees.csv"'
    writer = csv.writer(response)
    writer.writerow(['Receipt No', 'Roll No', 'Student Name', 'Description', 'Amount', 'Paid', 'Status', 'Due Date', 'Paid Date'])
    for r in FeeRecord.objects.select_related('student').all():
        writer.writerow([
            r.receipt_number, r.student.roll_number, r.student.get_full_name(),
            r.description, r.amount, r.amount_paid, r.get_status_display(),
            r.due_date, r.paid_date or ''
        ])
    return response


@login_required
def fee_structure_list(request):
    structures = FeeStructure.objects.select_related('department').all()
    return render(request, 'fees/structure_list.html', {'structures': structures})


@login_required
def fee_structure_create(request):
    if request.method == 'POST':
        form = FeeStructureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fee structure created.')
            return redirect('fees:structure_list')
    else:
        form = FeeStructureForm()
    return render(request, 'fees/structure_form.html', {'form': form})


def _send_fee_receipt_email(record):
    from django.core.mail import send_mail
    send_mail(
        subject=f'Fee Receipt - {record.receipt_number}',
        message=f'Dear {record.student.get_full_name()},\n\nYour payment of ₹{record.amount_paid} has been received.\nReceipt No: {record.receipt_number}\n\nThank you.',
        from_email=None,
        recipient_list=[record.student.email],
        fail_silently=True,
    )
