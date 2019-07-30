from django.contrib import admin

# Register your models here.
from .models import Snack
from .models import Request
from .models import Image, Tag, Like, Operation, User, Dislike

admin.site.register(Snack)
admin.site.register(Request)
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Dislike)


