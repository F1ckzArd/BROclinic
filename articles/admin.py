from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from .models import Article

# Register your models here.


class ArticleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


admin.site.register(Article, ArticleModelAdmin)