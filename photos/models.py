from django.db import models
from django.utils.safestring import mark_safe 


# Create your models here.


class Post(models.Model):
	REGION_CHOICES = (
			('Asia', 'Asia'),
			('N. America', 'N. America'),
			('S. America', 'S. America'),
			('Europe', 'Europe'),
			('Africa', 'Africa'),
		)
	title = models.CharField(max_length=200, blank=True)
	region = models.CharField(
			max_length=20,
			choices=REGION_CHOICES,
		)
	image = models.ImageField(null=True, blank=False, width_field="width", height_field="height")
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	summary = models.TextField()
	publish_date = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __str__(self):
		return self.title


	#order so that latest or most recently published posts appear at top
	class Meta:
		ordering = ["-publish_date"]


	def thumb_post(self):
		if self.image:
			addr = u'<img src="%s" style="width: 150px;" />' % self.image.url
			return mark_safe(addr)
		else:
			return 'No Image Found'



class Photo(models.Model):
	short = models.CharField(max_length=200, blank=True)
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	post = models.ForeignKey(
			'Post',
			on_delete=models.CASCADE,
			null=True,
		)
	image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	order = models.IntegerField(default=None)
	description = models.TextField(blank=True)


	def __str__(self):
		return self.short


	class Meta:
		ordering = ["order"]


	def thumb(self):
		if self.image:
			addr = u'<img src="%s" style="width: 150px;" />' % self.image.url
			return mark_safe(addr)
		else:
			return 'No Image Found'


