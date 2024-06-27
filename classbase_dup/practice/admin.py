from django.contrib import admin
from .models import Student, CustomUser
# Register your models here.

@admin.register(Student)         # for this admin page show our app and data
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','section','state','phone_no']
    # list_display=['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']

####################################################################################################################
                                       #Abstract_User Admin page Show

# @admin.register(CustomUser)                                
# class AbstractUser(admin.ModelAdmin):
#     list_display= [field.name for field in CustomUser._meta.fields if field.name != "id"]     # this is for all fields



####################################################################################################################
                                       #Abstract_Base_User Admin page Show


@admin.register(CustomUser)
class AbstractBaseAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined']
    # list_filter = ('is_staff', 'is_active')

    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Personal info', {'fields': ('first_name', 'last_name')}),
    #     ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login',)}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
    #     ),
    # )
    # search_fields = ('email',)
    # ordering = ('email',)