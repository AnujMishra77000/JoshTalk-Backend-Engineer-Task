from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Tasks.models import User, Task_Detail
from .serializers import TaskSerializer, UserSerilaizer, AssignTaskSerializer
from datetime import timedelta
from django.utils.timezone import now


# Class based api to create task using via POST method
class Task_Create_View(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():  # Check if the data is valid or not
            serializer.save() #if valid then save task to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
         # If provided data is not valid then it will shown error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Class based api to assign available task to user's via POST method, can assign one task multiple user's or single users also.
class Task_Assign_View(APIView):
    def post(self, request):
        task = AssignTaskSerializer(data=request.data)
        if task.is_valid():
            task_id = task.validated_data.get("task_id") # Validating task_id 
            user_id = task.validated_data.get("users") # Validating user
            
            completed_at  = now() + timedelta(hours=48) # Task completion time will be set while task assining to user
            try:
                task = Task_Detail.objects.get(id=task_id)# fetching task by task id
            except Task_Detail.DoesNotExist:
                return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

            users = User.objects.filter(id__in=user_id) # fething user by user id
            if not users.exists():
                return Response({"error": "No valid users found"},  status=status.HTTP_400_BAD_REQUEST)
              
            task.users.add(*users)
            task.completed_at= completed_at
            task.save() #saving model instance after performing all operations
            return Response({"message":"Users assigned successfully"},status=status.HTTP_200_OK)
        return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)

#Class based api view to retrive task to assign specific user's via GET method it gives users all assigned tasks
class UsersTask_View(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            task = UserSerilaizer(user)
            return Response(task.data, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({"error": "User  not found"}, status=status.HTTP_404_NOT_FOUND)


########################***** ADDITIONAL Api's To Track available Tasks and Users ******####################
        

class Task_and_User_List(APIView):
    def get(self,request):
        task=Task_Detail.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    
    def get(self, request):
        users=User.objects.all()
        serializer = UserSerilaizer(users, many=True)
        return Response(serializer.data)