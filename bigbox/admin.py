from django.contrib import admin
from .models import Reason, Category, Activity, Box

@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 7

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    list_editable = ['order']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 5

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'internal_name', 'category']
    list_editable = ['category']
    list_filter = ('reasons',)
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 20

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ['name', 'box_activities', 'slug']
    list_editable = ['slug']
    list_filter = ('category',)
    search_fields = ['activities__name']
    actions_on_top = False
    actions_on_bottom = True
    list_per_page = 20

    def box_activities(self, obj):
        return ", ".join([activity.name for activity in obj.activities.all().order_by("name")[:3]])
    box_activities.short_description = "Experiencias" 