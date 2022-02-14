from django.contrib import admin
from .models import Bb
from .models import Rubric
from .models import User

class BbAdmin(admin.ModelAdmin) :
	list_display = ('title', 'content', 'price', 'published', 'rubric', 'user')
	list_display_links = ('title', 'content')
	search_fields = ('titile', 'content', 'price', 'published')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
admin.site.register(User)

# Register your models here.
