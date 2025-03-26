from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Tasks.models import User, Task_Detail
from .serializers import TaskSerializer, UserSerilaizer, AssignTaskSerializer
from datetime import timedelta
from django.utils.timezone import now



class Task_Create_View(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():  # Check if the data is valid or not
            serializer.save() #if valid then save task to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
         # If provided data is not valid then it show's error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Task_Assign_View(APIView):
    def post(self, request):
        task = AssignTaskSerializer(data=request.data)
        if task.is_valid():
            task_id = task.validated_data.get("task_id")
            user_id = task.validated_data.get("users")
            
            completed_at  = now() + timedelta(hours=48)
            print(f"Task should be completed at:{completed_at}")
            try:
                task = Task_Detail.objects.get(id=task_id)
            except Task_Detail.DoesNotExist:
                return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

            users = User.objects.filter(id__in=user_id) 
            if not users.exists():
                return Response({"error": "No valid users found"},  status=status.HTTP_400_BAD_REQUEST)
              
            task.users.add(*users)
            task.completed_at= completed_at
            task.save()
            return Response({"message":"Users assigned successfully"},status=status.HTTP_200_OK)
        return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)


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