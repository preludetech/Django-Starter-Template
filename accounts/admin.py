# from django.contrib import admin
# from unfold.admin import ModelAdmin

# from django.contrib.auth.models import User, Group

# admin.site.unregister(User)
# admin.site.unregister(Group)
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

# User = get_user_model
# from .models import User


admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
