from django.contrib import admin
from .models import *
# Register your models here.

class Volunteer_Admin(admin.ModelAdmin):
	list_display = ('v_id','v_name','v_mob','v_image','join_date')
	search_fields = ('v_id','v_name')
	#readonly_fields = ('user_name','date')
    #filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

class Lab1_Admin(admin.ModelAdmin):
	list_display = ('v_id','v_name','lastvisit_date','visit_no')
	search_fields = ('v_id','v_name')

class Lab2_Admin(admin.ModelAdmin):
	list_display = ('v_id','v_name','lastvisit_date','visit_no')
	search_fields = ('v_id','v_name')

class Lab3_Admin(admin.ModelAdmin):
	list_display = ('v_id','v_name','lastvisit_date','visit_no')
	search_fields = ('v_id','v_name')

class Lab4_Admin(admin.ModelAdmin):
	list_display = ('v_id','v_name','lastvisit_date','visit_no')
	search_fields = ('v_id','v_name')

class VistedData_Admin(admin.ModelAdmin):
	list_display = ('v_id','v_name','visit_date','entry_time','going_time','lab_no',
					'reason','last_visit')


admin.site.register(Volunteer,Volunteer_Admin)
admin.site.register(Visited_data,VistedData_Admin)
admin.site.register(Lab1,Lab1_Admin)
admin.site.register(Lab2,Lab2_Admin)
admin.site.register(Lab3,Lab3_Admin)
admin.site.register(Lab4,Lab4_Admin)
