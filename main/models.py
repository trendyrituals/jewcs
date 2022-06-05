from django.db import models

# Create your models here.
class Detail(models.Model):
	name = models.CharField(blank=False,max_length=255)
	img = models.ImageField(blank=False)
	about = models.TextField(blank=False)
	extra = models.TextField(blank=True)

	def __str__(self):
		return self.name


class Certificate(models.Model):
	name = models.CharField(blank=False,max_length=255)
	img = models.ImageField(blank=False)

	def __str__(self):
		return self.name

class Gallery(models.Model):
	name = models.CharField(blank=False,max_length=255)
	img = models.ImageField(blank=False)

	def __str__(self):
		return self.name


class Logo(models.Model):
	name = models.CharField(blank=False,max_length=255)
	logo = models.ImageField(blank=False)

	def __str__(self):
		return self.name


class Welfare_measures(models.Model):
	title = models.CharField(blank=False,max_length=255)
	details = models.TextField(blank=False)

	def __str__(self):
		return self.title


class Feathers_to_our_cap(models.Model):
	title = models.CharField(blank=False,max_length=255)
	details = models.TextField(blank=False)

	def __str__(self):
		return self.title


class Contact_info(models.Model):
	title = models.CharField(blank=False,max_length=255)
	address_first = models.CharField(blank=False,max_length=255)
	address_second = models.CharField(blank=True,max_length=255)
	email = models.CharField(blank=False,max_length=255)
	number_first = models.CharField(blank=True,max_length=255)
	number_second = models.CharField(blank=True,max_length=255)

	def __str__(self):
		return self.title



class Security_training(models.Model):
	title =models.CharField(blank=False,max_length=255)
	details = models.TextField(blank=False)
	img = models.ImageField(blank=False)

	def __str__(self):
		return self.title


class Management_of_tolls(models.Model):
	title = models.CharField(blank=False,max_length=255)
	first_detail = models.TextField(blank=False)
	second_detail = models.TextField(blank=True)
	third_detail = models.TextField(blank=True)
	fourth_detail = models.TextField(blank=True)
	img = models.ImageField(blank=False)

	def __str__(self):
		return self.title

class Mission(models.Model):
	title = models.CharField(blank=False, max_length=255)

	def __str__(self):
		return self.title


class Vision(models.Model):
	title = models.CharField(blank=False,max_length=255)

	def __str__(self):
		return self.title


class Vast_Network(models.Model):
	txt = models.TextField(blank=False)

	def __str__(self):
		return "Vast Network"



class Board_of_directors(models.Model):
	name = models.CharField(blank=False,max_length=255)
	position = models.CharField(blank=False,max_length=255)

	def __str__(self):
		return self.name


class Our_Clients(models.Model):
	name = models.CharField(blank=False,max_length=255)

	def __str__(self):
		return self.name

























