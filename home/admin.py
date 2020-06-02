from django.contrib import admin
from .models import *



class ArticleToReadAdmin(admin.ModelAdmin):
    #list_display = ["name"]
    list_display = [field.name for field in ArticleToRead._meta.fields]
    search_fields = ["name"]

    class Meta:
        model = ArticleToRead

admin.site.register(ArticleToRead,ArticleToReadAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name_category"]
    search_fields = ["name"]

    class Meta:
        model=Category

admin.site.register(Category,CategoryAdmin)