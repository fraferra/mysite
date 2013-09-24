from django.contrib import admin
from ciip.models import UserProfile

class CiipAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields':['first_name','last_name','email','password']}),
        ('Academic Information', {'fields':['university']}),
    ]
    list_display = ('first_name', 'last_name',)

admin.site.register(UserProfile, CiipAdmin)
