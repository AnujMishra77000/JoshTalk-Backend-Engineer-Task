from django.urls import path
from .views import Task_Create_View, Task_Assign_View, UsersTask_View, Task_and_User_List

urlpatterns = [
    path('create/', Task_Create_View.as_view(), name='task_Creat'),
    path('assign/', Task_Assign_View.as_view(), name='task_assign'),
    path('users_tasks/<int:user_id>/',UsersTask_View.as_view(), name='user_tasks' ),


    #########**** Additonal Api ****#########
    path('Tlist/', Task_and_User_List.as_view(), name='task_list'),
    path('Ulist/', Task_and_User_List.as_view(), name='user_list')
]
