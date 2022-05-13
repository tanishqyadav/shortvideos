API to take Video_file Input & Save them to DB as well as in Static Folder, it's also perform deletion of the video_file from the DB and as from the static folder under the name of svideo API

All the Depedencies are in requirements.txt 

cd socialmedia 
py manage.py makemigrations
py manage.py migrate
py manage.py makesuperuser
py manage.py runserver

https://localhost/ #forshowing the user's video input 

https://localhost/admin #for taking the video file input from the user

https://localhost/delete/<int> #for deleting video_file 