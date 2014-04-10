from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'automechanic.views.home', name='home'),
    # url(r'^automechanic/', include('automechanic.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('automechanic.authentication.views',
    url('^[/]?$', 'login', name='login'),
    url(r'^login/$', 'login', name='login'),
)

urlpatterns += patterns('automechanic.client.views',

    url(r'^client/list/', 'list_all', name='client.list'),
    url(r'^client/add/', 'add', name='client.add'),
    url(r'^client/save/', 'save', name='client.save'),
    url(r'^client/edit/(?P<client_id>\d+)[/]?$', 'edit', name="client.edit",),
    url(r'^client/update/(?P<client_id>\d+)[/]?$', 'update', name="client.update",),
)
