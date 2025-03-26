JoshTalk Backend Engineer Python/Django Task Submission

Since there's no mention of user registration, authentication, or role-based access, 
we will assume that users are pre-existing in the system.

Features
1) Task Creation Api (Users can create new tasks with a name and description.)
2) Task Assignment Api (Tasks can be assigned to one or multiple users.)
3) Retrieve Assigned Tasks Api (Fetch tasks assigned to a specific user.)

Installations (install all in venv activated environment)
install django --> pip install django
install Restframework --> pip install Djangorestfreamwork

project Structure
Task_Management
-- settings.py  (where app and rest_framework are add inside Installed_aaps)
-- urls.py     (Project level urls who redirects to app level urls path)
--Tasks
    -- models.py (where all models are declared related proeject)
    -- admin.py (all models are register)
    -- Api (folder inside Tasks to develop all api related stuff)
       -- serializers.py (all models serializers)
       -- urls.py        (all api urls endpoints)
       -- views.py      (all Api's and business logic's)

       
Output:-
1) api_view:- Task_Create_View
endpoints 127.0.0.1:8000/task/create/
Response :-
{
    "id": 5,
    "task_name": "create final task Testing",
    "task_type": "Testing and designing",
    "description": "task to complete to run and execute and test",
    "created_at": "2025-03-26T09:01:06.435978Z",
    "completed_at": null,
    "status": true
}

2) api_view:- Task_Assign_View
endpoints 127.0.0.1:8000/task/assign/
Request body:- {  
    "task_id": 1,
    "users": [2, 3] <-- single user or multiple user 
}  
Response :-
{
    "message": "Users assigned successfully"
}

3) api_view:- UsersTask_View
endpoints 127.0.0.1:8000/task/users_task/<int:user_id>
Request body:- {
    "id": 1,
    "name": "Raam ji",
    "email": "ram@12.com",
    "mobile": "8797947490",
    "age": 18,
    "tasks": [
        {
            "id": 1,
            "task_name": "create task Backend",
            "task_type": "Backend",
            "description": "task to complete to run and execute the api for testing",
            "created_at": "2025-03-26T08:38:47.897478Z",
            "completed_at": "2025-03-28T08:57:42.901814Z",
            "status": true
        },
        {
            "id": 2,
            "task_name": "create task Frontend",
            "task_type": "Frontend",
            "description": "task to complete to run and execute the api for showw perpouses",
            "created_at": "2025-03-26T08:46:04.176086Z",
            "completed_at": "2025-03-28T11:03:41.291734Z",
            "status": true
        },
        {
            "id": 3,
            "task_name": "create task Webpage",
            "task_type": "WepApp",
            "description": "task to complete to run and execute the api for web aplication",
            "created_at": "2025-03-26T08:46:34.658487Z",
            "completed_at": "2025-03-28T11:03:47.535258Z",
            "status": true
        },
        {
            "id": 4,
            "task_name": "create task Testing",
            "task_type": "Testing and designing",
            "description": "task to complete to run and execute the api for web for testing and designing",
            "created_at": "2025-03-26T08:47:08.533735Z",
            "completed_at": "2025-03-28T11:03:51.517953Z",
            "status": true
        }
    ]
}

All Task related files and there usage

models.py 
two models are there as per task requirements
1) User    (use to store user's related data)
2) Task_Detail (use to store Task related data)
As per task these both models are related between ManayToManay Relationship.

API (this folder located inside the (Tasks) App directory.
There are three files which is required to make APi
i)Serializers.py
   Inside the serilaizers.py three serializers are declared as per requirements
    1)TaskSerializer  
    2)UserSerializer  
    3)AssignTaskSerializer 
    
ii)Views.py
   Here inside the views.py implemented API's for Task_Create_View, Task_Assign_View, UsersTask_View 
   for specific user ensuring proper serialization and business logic handling.

iii) Urls.py 
    In urls.py defined API endpoints for Task_Create_View, Task_Assign_View, UsersTask_View
    Task_Create_View  --> localhost:8000/task/create/
    Task_Assign_View  --> localhost:8000/task/assign/
    UsersTask_View    --> localhost:8000/task/users_task/1    
   
   
 


