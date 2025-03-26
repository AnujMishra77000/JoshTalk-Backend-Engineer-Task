from rest_framework import serializers
from Tasks.models import Task_Detail, User

#Task serilaizer to serialize and validate the data which are comming from post method
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task_Detail
        fields= ['id', 'task_name', 'task_type', 'description', 'created_at','completed_at','status']
        extra_kwargs = {'users': {'read_only': True, 'write_only': True}, #Putting users, and completed_at in extra_kwargs, dont want users list in Response of single user request
                        'completed_at':{'read_only':True}}# dont want to set completion time while creation of task task ,completion time should be decided while Assigning task  

#User Serializer to serialize and validate users data and give proper response as per api request.
class UserSerilaizer(serializers.ModelSerializer): 
    tasks = TaskSerializer(many=True, read_only=True) # intention to add this line while retriving users assigined task with the information
                                                      # of user task assigend task should be there
    class Meta:
       model= User 
       fields=['id', 'name', 'email', 'mobile', 'age', 'tasks']    


#AssignTaskSerilaizer to serialize and validate data while assigning the task to single or multiple users
#intension to define AssignTaskSerializer because of if we are use TaskSerializer then we can not assign task to the user because of 
#while creation of task we dont want to assign the task to user but TaskSerializer model expecting the users so we set users in extra_kwargs and TaskSerializer 
# not capable to do this operation.                          
class AssignTaskSerializer(serializers.ModelSerializer):
     completed_at= serializers.DateTimeField(required=False, allow_null=True) 
     class Meta:
         model = Task_Detail
         fields= ['task_id','users', 'completed_at']
         extra_kwargs = {'task_name': {'read_only': True, 'write_only': True},
                         'description':{'read_only': True, 'write_only': True},
                         'task_type ': {'read_only': True, 'write_only': True}
                         }
     task_id = serializers.CharField(required=True)
     users = serializers.ListField(
         child = serializers.IntegerField(), required =True
     )# to pass multiple user id in list form
     