from django.contrib import admin
from .models import *
from .forms import StudentInformationForm

admin.site.register(Banner)
# admin.site.register(Product)

class StudentInformationAdmin(admin.ModelAdmin):
    form = StudentInformationForm
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')
    list_filter = ('first_name',)

    
admin.site.register(StudentInformation, StudentInformationAdmin)
admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title","color"]}

admin.site.register(SubCategory)


admin.site.site_header = "My Project"
admin.site.site_title = "My Project Title"
admin.site.index_title = "My Project Index"