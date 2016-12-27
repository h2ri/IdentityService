from django.contrib import admin
from .models import Policy, Role, RolePolicy

admin.site.register(Policy)
admin.site.register(Role)
admin.site.register(RolePolicy)