from django.contrib import admin

# Register your models here.


from django.contrib import admin
from StudentHelp.models import Word
from StudentHelp.models import Poll
from StudentHelp.models import Choice


class WordAdmin(admin.ModelAdmin):
    dictionary = ['word', 'finnish_translation']

admin.site.register(Word, WordAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']


admin.site.register(Poll, PollAdmin)