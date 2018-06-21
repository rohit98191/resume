from django.contrib import admin
from .models import Required
# Register your models here.
#class SkillerInline(admin.StackedInline):
 #   model =Skiller
  #  extra =1


class RequiredAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['name']}),
               ('Email_address',{"fields":['email_id']}),
               ('Phone No', {'fields': ['phone_no']}),
               ("City Name", {'fields': ['city']}),
               ("Education Details", {'fields': ['be_cgpa','hsc_percent','ssc_percent']})]
    #inlines =[SkillerInline]
admin.site.register(Required,RequiredAdmin)
#admin.site.register(Skiller)
#admin.site.register(Skiller)
#admin.site.register(Education)
#admin.site.register(Skills)
#admin.site.register(skiller)