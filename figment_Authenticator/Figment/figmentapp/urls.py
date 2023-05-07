from django.contrib import admin

from django.urls import path
from figmentapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("scanner", views.scanner, name='scanner'),
    path("admin_login", views.admin_login, name='admin_login'),
    path("contact", views.contact, name='contact'),
    path("new_admin", views.new_admin, name='new_admin'),
    path("admin_dashboard", views.admin_dashboard, name='admin_dashboard'),
    path("new_employee", views.new_employee, name='new_employee'),
    path("logout/", views.LogoutPage, name='logout')
]
