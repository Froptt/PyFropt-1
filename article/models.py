from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
	author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar Adı")
	title=models.CharField(max_length=50,verbose_name="Konu")
	content=RichTextField(max_length=1000,verbose_name="İçerik (255) Karakter")
	created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
	article_image = models.FileField(blank=True, null=True, verbose_name="Resim Ekle")
	def __str__(self):
		return f" Yazar {self.author} - Başlık {self.title}"
	
	class Meta:
		ordering = ['-created_date']  # tersen sıralıyor




	

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
	comment_author = models.CharField(max_length=50, verbose_name="İsim")
	comment_content = models.CharField(max_length=200, verbose_name="Yorum")
	comment_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.comment_content
	
	class Meta:
		ordering = ['-comment_date']


class pro(models.Model):
	article = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
	pro_name = models.CharField(max_length=50, verbose_name="İsim")
	pro_lasname = models.CharField(max_length=200, verbose_name="Yorum")

