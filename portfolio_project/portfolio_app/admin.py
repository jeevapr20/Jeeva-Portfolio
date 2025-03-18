from django.contrib import admin
from .models import ContactMessage
from portfolio_app.models import Project


# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')  # Fields to display in the admin list view
    search_fields = ('name', 'email', 'subject')  # Add search functionality
    list_filter = ('created_at',)  # Add filter by date
