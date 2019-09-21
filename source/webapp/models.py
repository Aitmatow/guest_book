from django.db import models
DEFAULT_STATUS = 'active'
STATUS_CHOICES = [(DEFAULT_STATUS, 'Активно'), ('blocked', 'Заблокировано')]

# Create your models here.
class Records(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,verbose_name='Имя автора')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='E-mail автора')
    record = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст записи')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    edited_date = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    status = models.CharField(max_length=15, null=False, default=DEFAULT_STATUS, blank=False, verbose_name='Статус', choices=STATUS_CHOICES)
