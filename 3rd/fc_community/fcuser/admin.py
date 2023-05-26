from django.contrib import admin
from .models import Fcuser

# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password') # 어드민페이지에서 표시할 필드가 리스트업되게

admin.site.register(Fcuser, FcuserAdmin)