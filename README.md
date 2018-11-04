# Django를 이용한 ToDo List app

## Develop environment
  - Windows 10

## Screenshot
task list page : ![ad1](https://user-images.githubusercontent.com/28725891/47963266-e05bc300-e06c-11e8-8bf5-22caee7d00c3.jpg)
task add page : ![ad - 1](https://user-images.githubusercontent.com/28725891/47963270-f2d5fc80-e06c-11e8-97eb-4cd701482f3d.jpg)

## Installation
  - ### pip install -r requirements.txt
  - ### python manage.py migrate
  - ### python manage.py runserver(default: http://localhost:8000)

## feature
  - ### task add, edit, delete
  - ### properties of task(* : required)
    - #### *Title
    - #### *Description
    - #### *Priority
    - #### Due Date
    - #### Completion
  - ### print message on list page when uncompleted task is outdated
