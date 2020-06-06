"""spotlightproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import include, path
from Home import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('Home.urls')),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('gd/<int:id>', views.gd),
    path('ppt/<int:id>', views.ppt),
    path('gdsubmit/<int:id>', views.gdsubmit),
    path('pptsubmit/<int:id>', views.pptsubmit),
    path('pptevaluation/<int:id>', views.pptevaluation),
    path('deletewinner/<int:id>', views.deletewinner),
    ]

