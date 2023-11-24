from django.urls import path
from django.contrib import admin
from .views import (
    userClientModelView,
    home,
    main_menu_view
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view = home, name="home"),
    path("client/", view = userClientModelView, name="client"),
    path("client/main/", view = main_menu_view, name="main")
]
