import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.update(result_expires=3600,
                enable_utc=True,
                timezone='UTC', )

app.conf.beat_schedule = {
    "every day between 12 AM": {
        "task": "check_overdue_loans",
        "schedule": crontab(hour=0, minute=0)
    }
}
