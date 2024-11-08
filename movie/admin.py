from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.template.defaultfilters import title

# Register your models here.
from .models import Movie,Review
# admin.site.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('title','description')
#     search_fields = ['title', 'description']
#     list_editable = ('description',)
# admin.site.register(Movie,MovieAdmin)
admin.site.register(Movie)
admin.site.register(Review)
