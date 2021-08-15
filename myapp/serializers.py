from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    student_marks_in_subjects = serializers.CharField(source='marks_of_student_in_subjects')
    class Meta:
        model = Student
        fields = [   
            'id',
            'student_name', 
            'student_roll_no',
            'student_class', 
            'passing_status',
            'student_school_name',
            'date_of_report',
            'student_email',
            'student_marks_in_subjects']   

    def update(self,instance,validated_data):
        instance.student_email  = validated_data.get('student_email', instance.student_email)
        instance.student_roll_no  = validated_data.get('student_roll_no', instance.student_roll_no)
        instance.student_class  = validated_data.get('student_class', instance.student_class)
        instance.passing_status  = validated_data.get('passing_status', instance.passing_status)
        instance.student_school_name  = validated_data.get('student_school_name', instance.student_school_name)
        instance.date_of_report  = validated_data.get('date_of_report', instance.date_of_report)
        instance.student_name  = validated_data.get('student_name', instance.student_name)

        instance.save()

        return instance   

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'

class MarksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marks
        fields = '__all__'

class CeleryTaskJobStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = CeleryTaskJobStatus
        fields = ['job_id','job_status']

