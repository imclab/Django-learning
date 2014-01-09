from django.contrib import admin

# Register your models here.


from django.contrib import admin
from StudentHelp.models import Word

class WordAdmin(admin.ModelAdmin):
    dictionary = ['word', 'finnish_translation']

admin.site.register(Word, WordAdmin)