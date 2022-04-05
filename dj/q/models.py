from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class City(models.Model):
	class Meta:
		verbose_name = 'Город'
		verbose_name_plural = 'Города'
	def __str__(self):
		return self.name
	name = models.CharField(max_length=200)

class Client(models.Model):
	class Meta:
		verbose_name = 'Клиент'
		verbose_name_plural = 'Клиенты'
	name = models.CharField(max_length=200)
	contact = models.CharField(max_length=200)
	cashback = models.IntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, blank=True, null=True)
	def __str__(self):
		return self.contact

class Partner(models.Model):
	class Meta:
		verbose_name = 'Партнёр'
		verbose_name_plural = 'Партнёры'
	name = models.CharField(max_length=200)
	contact = models.CharField(max_length=200)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

class TimeSlot(models.Model):
	class Meta:
		verbose_name = 'Временное окно'
		verbose_name_plural = 'Временные окна'
		constraints = [models.UniqueConstraint(fields=['text'], name='unique text')]
	def __str__(self):
		return self.text
	text = models.CharField(max_length=200)

class Quest(models.Model):
	class Meta:
		verbose_name = 'Квест'
		verbose_name_plural = 'Квесты'
	def __str__(self):
		return self.name
	name = models.CharField(max_length=200)
	price = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	socialMedia = models.CharField(max_length=200)
	playersCount = models.CharField(max_length=200)
	partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
	photo = models.FileField(null=True, default=None)
	timeslot_list = models.ManyToManyField(TimeSlot)
	city = models.ForeignKey(City, on_delete=models.CASCADE)


class PhotoAux(models.Model):
	photo = models.FileField(null=True, default=None)
	quest = models.ForeignKey(Quest, on_delete=models.CASCADE)

class Order(models.Model):
	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'
	quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	date = models.DateTimeField('Время заказа')
	timeslot = models.ForeignKey(TimeSlot, on_delete=models.PROTECT, null=True, default=None)

class Review(models.Model):
	class Meta:
		verbose_name = 'Обзор'
		verbose_name_plural = 'Обзоры'
	quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)

class Discount(models.Model):
	class Meta:
		verbose_name = 'Скидка'
		verbose_name_plural = 'Скидки'
	quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
