from django.contrib import admin

from plagiarism.models import Result, File1, File2

admin.site.register(Result)
# admin.site.add_action(Results)
admin.site.register(File1)
admin.site.register(File2)

# Register your models here.
