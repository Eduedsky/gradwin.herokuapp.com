"""gradwin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from inventory.views import product_details, category_details
# from manager import views
# from authentication import views


urlpatterns = [
    path('', include("authentication.urls")),
    path('admin/', admin.site.urls),
    path('manager/', include("manager.urls")),
    path('inventory/', include("inventory.urls")),
    path('sales/', include("sales.urls")),
    # path('<slug:category_slug>/<slug:slug>/',
    #      product_details, name="product_details"),
    # path('<slug:slug>/', category_details, name="category_details"),


    # path('logout', views.logout, name="logout"),

]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
