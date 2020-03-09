"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from django.conf.urls import url, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

import question.api

router = routers.DefaultRouter()
router.register('questions', question.api.QuestionViewSet)
router.register('answers', question.api.AnswerViewSet)
router.register('users', question.api.UserViewSet)

schema_url_v1_patterns = [
    url(r'^api/v1/', include((router.urls, 'question'), namespace='api')),
]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="Aziro's Open API for Shariq",
        default_version='v1',
        description="Hi, This is a page of aziro's open api for Shariq",
        terms_of_service="",
        contact=openapi.Contact(email="talent.dev.guru@gmailc.om"),
        license=openapi.License(name=""),
    ),
    validators=['flex'],  # 'ssv'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_v1_patterns,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include((router.urls, 'member'), namespace='api')),

    # Auto DRF API docs
    url(r'^swagger(?P<format>\.json|\.yaml)/v1$',
        schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/v1/$', schema_view_v1.with_ui('swagger',
                                                 cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/v1/$', schema_view_v1.with_ui('redoc',
                                               cache_timeout=0), name='schema-redoc-v1'),
]
