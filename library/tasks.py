from celery import shared_task
from .models import Loan
from django.core.mail import send_mail
from django.conf import settings
from .models import Loan
from datetime import datetime

@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass


@shared_task(bind=True, name='check_overdue_loans')
def check_overdue_loans(self):
    current_date = datetime.today()
    loan_objects = Loan.objects.filter(is_returned=False, due_date_lt=current_date)
    for loan in loan_objects:
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Reminder Overdue Loan',
            message=f'Hello {loan.member.user.username},\n\nYour due date has been passed "{book_title}".\nPlease return it tot the library.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )



