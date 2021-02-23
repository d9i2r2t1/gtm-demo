from django.contrib import admin

from gtm_demo.models import DemoLanding

admin.site.site_header = 'GTM demo landings'
admin.site.site_title = 'GTM demo landings'


class DemoLandingAdmin(admin.ModelAdmin):
    list_display = ('id', 'gtm_id', 'hashcode', 'created_at')
    list_display_links = ('id', 'gtm_id')
    search_fields = ('gtm_id', 'hashcode')


admin.site.register(DemoLanding, DemoLandingAdmin)
