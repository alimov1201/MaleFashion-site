from django.contrib import admin

from article.models import Article, Contact, Email


admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Email)
