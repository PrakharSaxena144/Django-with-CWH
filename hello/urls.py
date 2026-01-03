"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Every request to Django first goes through this file to determine how to route the request. Then to specific apps.
# Django have default authentication system and admin apps.
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Prakhar Admin"
admin.site.site_title = "Main Manager Admin Portal"
admin.site.index_title = "Welcome to Maps Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Including URLs from the 'home' app
]
