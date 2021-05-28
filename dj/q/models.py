from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
	class Meta:
		verbose_name = 'Клиент'
		verbose_name_plural = 'Клиенты'
	name = models.CharField(max_length=200)
	contact = models.CharField(max_length=200)
	cashback = models.IntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Partner(models.Model):
	class Meta:
		verbose_name = 'Партнёр'
		verbose_name_plural = 'Партнёры'
	name = models.CharField(max_length=200)
	contact = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Quest(models.Model):
	class Meta:
		verbose_name = 'Квест'
		verbose_name_plural = 'Квесты'
	name = models.CharField(max_length=200)
	partner = models.ForeignKey(Partner, on_delete=models.CASCADE)

class Order(models.Model):
	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'
	quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	date = models.DateTimeField('Время заказа')

class Review(models.Model):
	class Meta:
		verbose_name = 'Обзор'
		verbose_name_plural = 'Обзоры'
	quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)