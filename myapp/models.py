from django.db import models

# Create your models here.
class Student(models.Model):
    Passing_Status_Choices = (
        ('Pass','Pass'),
        ('Fail','Fail')
    )
    student_name = models.CharField(max_length=200)
    student_roll_no = models.IntegerField(unique=True)
    student_class = models.CharField(max_length=200)
    passing_status = models.CharField(choices=Passing_Status_Choices,max_length=4,default=None, null=True,blank=True)
    student_school_name = models.CharField(max_length=200)
    date_of_report = models.DateField(auto_now_add=True)
    student_email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.student_name
    
    @property
    def marks_of_student_in_subjects(self):
        lst_of_marks_sub = {}
        student_id = Marks.objects.values('student').distinct()

        for i in student_id:
            student_subject_and_marks = Marks.objects.filter(student=i['student']).values('students_marks','student_subject')
            for data in student_subject_and_marks:
                subject_id_fetch = data['student_subject']
                subject_name_fetch = Subject.objects.get(pk=subject_id_fetch)
                subject_name = subject_name_fetch.name_of_subject
                student_mark_with_sub = int(data['students_marks'])
                lst_of_marks_sub[subject_name] = student_mark_with_sub

            return lst_of_marks_sub
           

class Subject(models.Model):
    name_of_subject = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name_of_subject
    
    
class Marks(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    student_subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    students_marks = models.FloatField()      


class CeleryTaskJobStatus(models.Model):
    job_id = models.CharField(max_length=1000)
    job_status = models.CharField(max_length=100)