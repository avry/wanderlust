from django.contrib import admin
from . models import Post, Photo
from django.utils.safestring import mark_safe 
from django.db import models
from django.contrib.admin.widgets import AdminFileWidget

# Register your models here.
# class AdminImageWidget(AdminFileWidget):
# 	def render(self, name, value, attr=None):
# 		output = []
# 		if value and getattr(value, "url", None):
# 			image_url = value.url
# 			file_name=str(value)
# 			output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: cover;"/></a> %s ' % (image_url, image_url, file_name, _('')))
# 		output.append(super(AdminFileWidget, self).render(name, value, attrs))
# 		return mark_safe(u''.join(output))


# class CollectionImageInline(admin.TabularInline):
# 	formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}



class PhotoInline(admin.StackedInline):
	fields = ( 'thumb', 'image', 'order', 'short', 'description', )
	readonly_fields = ('thumb',)
	model = Photo
	extra = 3



class PostAdmin(admin.ModelAdmin):
	fields = ('thumb_post', 'image',"title", "region", "summary")
	readonly_fields = ('thumb_post',)


	inlines = [PhotoInline]

	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)
