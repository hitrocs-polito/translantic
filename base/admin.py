from django.contrib import admin
from .models import Translator
# Register your models here.
class TranslatorAdmin(admin.ModelAdmin):
    list_display = ('english', 'uzbek')


admin.site.register(Translator, TranslatorAdmin)
