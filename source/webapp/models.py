from django.db import models


status_choices = [('new','Новая'),('in_progress', 'В процессе'),('done', 'Сделано')]


class Task(models.Model):
    description = models.TextField(max_length=300, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length = 12, verbose_name='Статус',
                              default= status_choices[0][0], choices=status_choices)
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Подробно')
    completed_at = models.DateField(null=True, blank=True, default=None, verbose_name='Время создания')

    def __str__(self):
        return self.description

