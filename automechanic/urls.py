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

'''
Client
'''
urlpatterns += patterns('automechanic.client.views',

    url(r'^client/list/', 'list_all', name='client.list'),
    url(r'^client/add/', 'add', name='client.add'),
    url(r'^client/save/', 'save', name='client.save'),
    url(r'^client/edit/(?P<client_id>\d+)/', 'edit', name="client.edit",),
    url(r'^client/update/(?P<client_id>\d+)/', 'update', name="client.update",),
    url(r'^client/delete/', 'delete', name='client.delete'),
)

'''
Vehicle
'''
urlpatterns += patterns('automechanic.vehicle.views',

    url(r'^vehicle/list/(?P<client_id>\d+)/', 'list_all', name='vehicle.list'),
    url(r'^vehicle/add/(?P<client_id>\d+)/', 'add', name='vehicle.add'),
    url(r'^vehicle/save/(?P<client_id>\d+)/', 'save', name='vehicle.save'),
    url(r'^vehicle/edit/(?P<vehicle_id>\d+)/', 'edit', name="vehicle.edit",),
    url(r'^vehicle/update/(?P<vehicle_id>\d+)/', 'update', name="vehicle.update",),
    url(r'^vehicle/delete/(?P<client_id>\d+)/', 'delete', name='vehicle.delete'),
)

'''
Part
'''
urlpatterns += patterns('automechanic.part.views',

    url(r'^part/list/', 'list_all', name='part.list'),
    url(r'^part/add/', 'add', name='part.add'),
    url(r'^part/save/', 'save', name='part.save'),
    url(r'^part/edit/(?P<part_id>\d+)/', 'edit', name="part.edit",),
    url(r'^part/update/(?P<part_id>\d+)/', 'update', name="part.update",),
    url(r'^part/delete/', 'delete', name='part.delete'),
)

'''
Employee
'''
urlpatterns += patterns('automechanic.employee.views',

    url(r'^employee/list/', 'list_all', name='employee.list'),
    url(r'^employee/add/', 'add', name='employee.add'),
    url(r'^employee/save/', 'save', name='employee.save'),
    url(r'^employee/edit/(?P<employee_id>\d+)/', 'edit', name="employee.edit",),
    url(r'^employee/update/(?P<employee_id>\d+)/', 'update', name="employee.update",),
    url(r'^employee/delete/', 'delete', name='employee.delete'),
)
