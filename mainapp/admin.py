from django.contrib import admin

# Register your models here.
from .models import userInfo,genre,articles,favgenres,favauthors,subscription,comments#,token

admin.site.register(userInfo)
admin.site.register(articles)
admin.site.register(genre)
admin.site.register(favgenres)
admin.site.register(favauthors)
admin.site.register(subscription)
admin.site.register(comments)
# 
#admin.site.register(Userprofile)