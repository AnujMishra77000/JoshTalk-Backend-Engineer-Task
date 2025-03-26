from rest_framework import serializers
from Tasks.models import Task_Detail, User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task_Detail
        fields= ['id', 'task_name', 'task_type', 'description', 'created_at','completed_at','status']
        extra_kwargs = {'users': {'read_only': True, 'write_only': True},
                        'completed_at':{'read_only':True}}  # users field 

class UserSerilaizer(serializers.ModelSerializer): 
    tasks = TaskSerializer(many=True, read_only=True) 
    class Meta:
       model= User 
       fields=['id', 'name', 'email', 'mobile', 'age', 'tasks']    

class AssignTaskSerializer(serializers.ModelSerializer):
     completed_at= serializers.DateTimeField(required=False, allow_null=True) 
     class Meta:
         model = Task_Detail
         fields= ['task_id','users', 'completed_at']
         extra_kwargs = {'task_name': {'read_only': True, 'write_only': True},
                         'description':{'read_only': True, 'write_only': True},
                         'task_type ': {'read_only': True, 'write_only': True}
                         }
     #task_type = serializers.CharField(required = True)
     task_id = serializers.CharField(required=True)
     users = serializers.ListField(
         child = serializers.IntegerField(), required =True
     )
     