from celery import shared_task
import time

import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


@shared_task
def celery_task(counter):
    email = "testing.email@gmail.com"
    time.sleep(30)
    return '{} Done!'.format(counter)


@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)