from django.contrib import admin

from core.models import Course,Testimonial,Gallery,News,Downloads,Contact

admin.site.site_header = 'AIMS College Admin Panel'
admin.site.site_title = 'Garima'
admin.site.index_title = 'Features area'                

# admin.site.enable_nav_sidebar = False
# Register your models here.
admin.site.register(Course)
admin.site.register(Testimonial)
admin.site.register(Gallery)
admin.site.register(News)
admin.site.register(Downloads)
admin.site.register(Contact)
