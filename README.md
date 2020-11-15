# QA-Fundamental-Project
## **Recipe App**

### **Resources**
* Presentation: https://docs.google.com/presentation/d/1E7wdMY3jFwsYQxpgYA3c2mv1r2Pufd_a_nhDwjqJK-k/edit#slide=id.ga9936a0ad4_0_5
* Trello Board: https://trello.com/b/8zRp5ZJX/recipe-project
* Website: http://35.242.141.26:5000/

### **Brief**
For this project, I had the objective of creating a web application that can create, read, update and delete (CRUD) as well as implement other methodologies learnt throughout the training. Some of these include a Trello Board, a relation database, clear design phases illustrating the architecture and a CI Pipeline.

### **My Approach**
I decided to base my application on recipes as cooking is a big hobby of mine. I envisioned an application that allows users to read recipes posted by others, as well as upload their own. In order to achieve this, users could do the following:

* Create an ingredients list that stores just the name.
* Create a method that stores the steps to a recipe, as well as the expected time duration.
* Create a recipe that stores:
  * The name of the recipe
  * The essential ingredients provided by the ingredients list
  * The relevant quantity for each ingredient
  * The relevant method for the recipe - provided by the method database
* View recipes posted
* Update or Delete recipes

### **Architecture** 

#### **Database Structure**
My final entity relationship diagram (ERD) illustrates the tables within my application and their many-to-many relationships:  
[Imgur](https://i.imgur.com/MWoI9Uz.png)

#### **CI Pipeline**
The CI Pipeline for my application:  
[Imgur](https://i.imgur.com/Zr9RNNB.jpg)

### **Project Tracking**
I chose to track my project using Trello and have attached a snapshot below.  
[Imgur](https://i.imgur.com/VmvJAbi.png)

I seperated my Trello board into five sections to clearly track my progress and I did this by having a to-do, doing and done section as well as a user story section in order to always have a clear vision of my application and finally a product backlog which contained the brief.

### **Risk Assessment**
The risk assessment I completed can be found here:  
https://docs.google.com/spreadsheets/d/15U51YRdiurGMEHM5TBIvR6X54iHQVbD6h4-d2rWDp7Y/edit?usp=sharing

I have also included a screenshot here:  
[Imgur](https://i.imgur.com/jwd9J1z.png)

### **Testing**
I completed my unit-tests using pytest and ran it both in my virtual machine and through Gunicorn on Jenkins. These tests check that my application runs and the functions do what I'm expecting them too. Here is a screenshot of my test coverage:  
[Imgur](https://i.imgur.com/01hOs70.png)

As you can see, I have an 82% test coverage and these tests include running of the application and valid submissions. Unfortunately, I am short of 100% coverage due to the fact I have not run tests on invalid submissions. For example, if I didn't input a name on the recipe form. Pytest is useful as it tells you which lines of code are not covered and so a future improvement will be for me to investigate these lines and implement tests for them.

Below is a screenshot of my application runnning through Gunicorn on Jenkins:  
[Imgur](https://i.imgur.com/sscnD5H.png)

### **Front-End Design**
The front-end of the app is what the user sees and functions themself. I have included screenshots of how a user can navigate around my app, once it is running with the URL.

Initially you are directed to the home page which includes a list of the recipes that have been added:  
[Imgur](https://i.imgur.com/Ak3SQ7I.png)  
Here is the form for inputting ingredients which redirects to a list of all ingredients in the database:  
[Imgur](https://i.imgur.com/siMxzYS.png)  
[Imgur](https://i.imgur.com/nevWUhf.png)  
Here is the method form where users can input the steps and time expected and once submitted are redirected to a different method page:  
[Imgur](https://i.imgur.com/0VF53QK.png)  
[Imgur](https://i.imgur.com/Aqz6sQx.png)  
Here is where users can put together a recipe that calls on an ingredient from the database as well as a method:   
[Imgur](https://i.imgur.com/tJGr4Dn.png)  
[Imgur](https://i.imgur.com/6hRpe8E.png)  

#### **Known Issues**
There are a few problems with my current application:

* When the user inputs a recipe, they are only able to select one ingredient which is problematic when trying to follow. However, the method does include all of the ingredients but ideally you could clearly see a list of them.
* My integration test isn't passing so would like that working and passing in order to confirm my application is working as a whole.

### **Future Improvements**
There are a number of improvements I would like to implement:

* Fix the issue mentioned previously.
* Allow people to specify cuisines so that users can get more information about a recipe they may not have seen before.
* Implement the option to include an image so that users can visulise the food.
* Improve the general look of my application with some colour.
* Get 100% test coverage so that there are no lines of code not accounted for.

### **Author**

Hannah Lister-Sims




