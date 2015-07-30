from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# Register your models here.

from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    form = SignUpForm


admin.site.register(SignUp, SignUpAdmin)
