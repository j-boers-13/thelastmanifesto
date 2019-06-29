from django.contrib import admin
from .models import Board,Topic,Post

for x in [Board,Topic,Post]:
    admin.site.register(x)
