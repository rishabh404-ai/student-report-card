from rest_framework import routers
from .views import *
from django.urls import path 
from .tasks import *

router = routers.DefaultRouter()
router.register('student-data',StudentViewSet,basename='student')
router.register('subjects',SubjectsViewSet,basename='subjects')
router.register('student-marks',StudentMarksViewSet,basename='student-marks')
router.register('initialise-celery',InitialiseCeleryViewSet,basename='initialise-celery')
router.register('generate-student-report',StartGeneratingReport,basename='generate-student-report')
router.register('check-job-status',CheckJobStatus,basename='check-job-status')

urlpatterns = [
    
] + router.urls

