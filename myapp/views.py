from django.shortcuts import render
from rest_framework import viewsets, response 
from .models import *
from .serializers import *
from subprocess import PIPE, Popen, STDOUT 
from celery.result import AsyncResult
import imp
# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    """
    View to check student data
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SubjectsViewSet(viewsets.ModelViewSet):
    """
    View to check subject
    """

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class StudentMarksViewSet(viewsets.ModelViewSet):
    """
    View to check student marks
    """

    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

def execute_celery_command():
    comand = 'celery -A mysite worker -l info --pool=solo'
    proc = Popen(comand,shell=True)      
    out = proc.communicate()[0]
    print (out)    

def execute_celery_command_2():
    comand = 'celery -A mysite beat -l INFO'
    proc = Popen(comand,shell=True)      
    out = proc.communicate()[0]
    print (out)    


def check_celery_task_status():
    celery_job_id = CeleryTaskJobStatus.objects.values('job_id')
    for job in celery_job_id:
        job_id = job['job_id']
        res = AsyncResult(job_id).state
        CeleryTaskJobStatus.objects.filter(job_id=job_id).update(job_status=res)     
    
    print('Completed')

class InitialiseCeleryViewSet(viewsets.ViewSet):
    """
    View to start generating the report & sending email with celery
    """
    
    def list(self,request):   
        execute_celery_command()        
        return response.Response({'status: success',
                                  'message: report sent to mail'})

class StartGeneratingReport(viewsets.ViewSet):
    """
    View to start generating the report & sending email with celery
    """
    
    def list(self,request):    
        execute_celery_command_2()
        return response.Response({'status: success',
                                  'message: report sent to mail'})


class CheckJobStatus(viewsets.ReadOnlyModelViewSet):
    """
    View to check celery job/task status
    """

    serializer_class = CeleryTaskJobStatusSerializer 

    def get_queryset(self):
        check_celery_task_status() 
        return CeleryTaskJobStatus.objects.order_by('-id')
    

    
  