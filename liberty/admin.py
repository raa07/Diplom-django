from django.contrib import admin
from .models import Book, Author, Department, Student, BookStudent, Category
from django.utils.html import format_html

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('lib_id', 'image_tag', 'title', 'count', 'author')
    list_display_links = ('lib_id', 'title')
    search_fields = ('title', 'content')

    def image_tag(self, obj):
        return format_html('<img src="/{}" style="max-width:100px;"/>'.format(obj.photo))

    image_tag.short_description = 'Image'

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(BookStudent)
admin.site.register(Category)

