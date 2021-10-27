from django.contrib import admin
from .models import Task, Tovar
from .models import FIO
# Register your models here.

admin.site.register(Task)

admin.site.register(FIO)

admin.site.register(Tovar)
