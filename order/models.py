# -*- coding: utf-8 -*-
from django.db import models


class Order(models.Model):
    NEW = 0
    CONFIRMED = 1
    PAID = 2

    STATUS_CHOICES = (
        (NEW, u'новый'),
        (CONFIRMED, u'подтвержденный'),
        (PAID, u'оплаченный')
    )
    created = models.DateTimeField(u'Дата создания', auto_now_add=True)
    status = models.PositiveIntegerField(u'Статус', max_length=10,
                                        choices=STATUS_CHOICES, default=NEW)
    customer = models.CharField(u'Имя', null=True, blank=True,
                                max_length=100)
    email = models.EmailField('email', null=True, blank=True)
    phone = models.CharField(u'телефон', null=True, blank=True, max_length=20)

    def __unicode__(self):
        return u'{0} от {1}'.format(self.STATUS_CHOICES[self.status][1],
                                    self.customer)