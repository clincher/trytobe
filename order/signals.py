# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail


def order_notifying(order):
    from_email = settings.FROM_EMAIL
    owners = settings.ADMINS
    admin_email_list = [owner[1] for owner in owners]
    subject = u'новая заявка на trytobe.ru от {0}'.format(order.customer)
    body = u'''зайдите в панель управления сайтом trytobe.ru что бы посмотреть
     новую заявку на участие в тренинге'''
    send_mail(subject, body, from_email, admin_email_list)
