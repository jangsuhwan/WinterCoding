#Django를 이용한 ToDo List app

##Develop environment
  - Windows 10

##Screenshot
task list page : ![ad1](https://user-images.githubusercontent.com/28725891/47963266-e05bc300-e06c-11e8-8bf5-22caee7d00c3.jpg)
task add page : ![ad - 1](https://user-images.githubusercontent.com/28725891/47963270-f2d5fc80-e06c-11e8-97eb-4cd701482f3d.jpg)


$ pip install -r requirements.txt
$ python manage.py syncdb
$ python manage.py runserver
Features
Requires Login
Users must be created via Django Admin
Create Task
Delete Task
Tag Tasks
Also provides filtering by tag name
Search Tasks
search by date
search by title
search by tag name
Single UI for most important tasks
creation, search, and deleting of tasks is all AJAX
###Includes many features inherited from Django:

Robust Admin
Supports multiple databases
Robust templating engine
