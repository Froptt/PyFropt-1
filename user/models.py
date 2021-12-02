from django.db import models
from ckeditor.fields import RichTextField
from phone_field import PhoneField


class Contact(models.Model):
	name = models.CharField(max_length=16, verbose_name="İsim")
	email = models.EmailField()
	phone = models.CharField(max_length=11, verbose_name="Telefon")
	message = models.TextField(verbose_name="Mesaj")
	
	def __str__(self):
		return self.email
	
	


