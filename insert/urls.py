
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


from django.conf.urls import url, include
from .views import StudentRecordView
admin.autodiscover()
router = routers.DefaultRouter()

urlpatterns=[
  url('admin/',admin.site.urls),
  url('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]


urlpatterns += format_suffix_patterns([
    # API to map the student record
    url('api/univstud/',
        StudentRecordView.as_view(),
        name='students_list'),
])