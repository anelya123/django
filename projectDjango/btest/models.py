from django.db import models

class Bb(models.Model):
	title = models.CharField(max_length=50, verbose_name='Товар')
	content = models.TextField(null=True, blank=True, verbose_name='Описание')
	price = models.FloatField(null=True, blank=True, verbose_name='Цена')
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
	rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Поезд')
	user = models.ForeignKey('User', null=True, on_delete=models.PROTECT, verbose_name='Пользователь')

	class Meta:
		verbose_name_plural = 'Объявления'
		verbose_name  = 'Объявление'
		ordering = ['-published']

class Rubric (models.Model):
	name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
	def _str_(self):
		return self.name
	
	class Meta:
		verbose_name_plural = 'Поезда'
		verbose_name = 'Поезд'
		ordering = ['name']
class User (models.Model):
	name = models.CharField(max_length=20, db_index=True, verbose_name='Пользователь')
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = 'Пользователи'
		verbose_name = 'Пользователь'
		ordering = ['name']

# Create your models here.
