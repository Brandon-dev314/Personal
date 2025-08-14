from django.contrib import admin
from .models import Project8
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project8,ProjectAdmin)