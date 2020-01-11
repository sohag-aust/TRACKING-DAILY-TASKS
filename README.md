
-> Application Name: Tracking Daily Works.

-> Used Framework: Django (Based on Python). 

-> Used Database: sqlite3 (Build-in in django)

-> Description: This is a Daily routine based application where a user can login with his account and keep a track for his daily tasks or upcoming tasks with Deadline.
			    This application has 3 parts.
			 
			    Like:
					 1) Upcoming Tasks: Where user can jot down the upcoming tasks with Deadline that he will done.
					 2) Completed Tasks: When user do a task, he will check it as completed and then this task will show into the completed task options.
					 3) Failed Tasks: When a tasks of an user passed the Deadline then it will show into the failed tasks table.
			 

-> Project Tools: Visual Studio Code

-> Browser: Google Chrome

-> Python version: python 3.7.3 
				   check version: python --version
				
-> Django version: 2.0
				   check version: python -m django --version
				
-> Pip version: pip --version

-> Install Django: python -m pip install django

-> Directory Name: TRACKING DAILY WORKS
				   In this directory my project is saved.
				
-> Start Project: django-admin startproject TodoApplication

-> Start an App: python manage.py startapp todoapp
				 in this app, All models, views, and templates will loaded as Django supports MVT framework instead of MVC framework.
				  
				  1) M - (Model): For data, where class are loaded which offers tables fileds for Database. (replace Model of MVC).
				  2) T - (Template): For designing the files. like: HTML. (replace View of MVC).
				  3) V - (View): Binding of Models and templates where developer can implement the methods for implementation purposes. (replace Controller of MVC).
			  
-> Run the application: Goes to project folder as manage.py file is there and then,
					    python manage.py runserver
					    then there will generate a url, which is: 127.0.0.1:8000   where, 8000 is the port and other is host 
					 
					  ? why use manage.py ?
						-> manage.py: A command-line utility that lets us interact with this Django project in various ways. 
						   we can read all the details about manage.py in: django-admin and manage.py.
						   

-> Project Admin: 127.0.0.1:8000/admin
			      create superuser from terminal and then sign in with admin
			   

-> Super User: super user has the power to maintain the site

				python manage.py create superuser
				
				1) username: shohag
				2) password: sohag12345
			

-> Users of the application: Those persons who can jot down their regular stuffs.
			
				--> username:
					1) Mr.Cse
					2) Mr.EEE
					3) Mr.Civil
					4) Mr.Tex
					5) Mr.Mecha
					6) Mr.Archi
					
				--> password: sohag12345 (for all the username)
				

-> For DataBase: used ORM technique(Object Relational Mapper) for binding the table fields from the class definitions.
			     for binding with tables it must run a command like:
						python manage.py makemigrations
						
				 then the migration file will generate. like: 0001_initial.py, which is the first migration files.
				 then migrate it to update the database tables.
						python manage.py migrate
					
				  Each time when remigrations applied it will generate a new migration file, with a continuous counting numbers like- 0002%.py, 0003%.py (% means any name as for migration fileds needs)
				  											
						