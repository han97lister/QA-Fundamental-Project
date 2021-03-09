# QA-Fundamental-Project
## **Recipe App**

### **Resources**
* Presentation: https://docs.google.com/presentation/d/1E7wdMY3jFwsYQxpgYA3c2mv1r2Pufd_a_nhDwjqJK-k/edit#slide=id.ga9936a0ad4_0_5
* Trello Board: https://trello.com/b/8zRp5ZJX/recipe-project
* Website: http://35.242.141.26:5000/

### **Contents**
* [Brief](#brief)
* [My Approach](#my-approach)
* [Architecture](#architecture)
  * [Database Structure](#database-structure)
  * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-end Design](#front-end-design)
  * [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)
* [Author](#author)
  

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
![erd][erd]  

Below are my previous ERDs so that you can see the progression of my application:   
![erd1][erd1]
![erd2][erd2] 
 

#### **CI Pipeline**
The CI Pipeline for my application:  
![CI_Pipeline][CI_Pipeline]  
This pipeline clearly illustrates the usage I had in supporting tools, methodologies and technologies taught throughout the training.

### **Project Tracking**
I chose to track my project using Trello and have attached a snapshot below.  
![Trello_Board][Trello_Board]

I seperated my Trello board into five sections to clearly track my progress and I did this by having a to-do, doing and done section as well as a user story section in order to keep a clear vision of my application and finally a product backlog which contained the brief. I also labelled my tasks in order to fit with the mark scheme of this peoject. Therefore, green was for programming/software development, red for testing, orange for software design and yellow for systems integration and build.  I also labelled the user stories with purple and blue for the presentation. This gave me a simple visulisation for the whole project and it's goals and enabled me to quickly move from one task to another without worrying about forgetting anything. 

### **Risk Assessment**
The risk assessment I completed can be found here:  
https://docs.google.com/spreadsheets/d/15U51YRdiurGMEHM5TBIvR6X54iHQVbD6h4-d2rWDp7Y/edit?usp=sharing

I have also included a screenshot here:  
![risk_assessment][risk_assessment]  
This screenshot shows that the risks I have outlined are mostly low impact which is positive but also reassuring to know that I have methodologies thought and planned out in case this risks became a reality. Risk assessments should always be on-going as add an application develops, so will the risks and room for error. 

### **Testing**
I completed my unit-tests using pytest and ran it both in my virtual machine and through Gunicorn on Jenkins. These tests check that my application runs and the functions do what I'm expecting them too. Here is a screenshot of my test coverage:  
![test_cov][test_cov]

As you can see, I have an 82% test coverage and these tests include running of the application and valid submissions. Unfortunately, I am short of 100% coverage due to the fact I have not run  successful tests on invalid submissions. For example, if I didn't input a name on the recipe form. Pytest is useful as it tells you which lines of code are not accounted for and so a future improvement will be for me to investigate these lines and implement successful tests for them.

I also attempted to complete a full integration test however wasn't able to obtain all passes. Below is a screenshot to show pytest completing tests in my integration test file but only passing 2/3 tests that were run:  
![test_int][test_int]  

It's good to use both unit-testing and integration testing as it allows you to prevent otherwise future problems. The balance of both means you've not only tested that your app does what you're expecting it to, but also that the user will have the same experience.

Below is a screenshot of my application runnning through Gunicorn on Jenkins:  
![jenkins][jenkins]  
Jenkins allows my app to run in the background giving more freedom when making changes as it doesn’t prevent the app from working like a virtual machine would. Jenkins is widely used as it is easily set up and configured as well as being free to download.

### **Front-End Design**
The front-end of the app is what the user sees and functions themself. I have included screenshots of how a user can navigate around my app, once it is running with the URL.

Initially you are directed to the home page which includes a list of the recipes that have been added:  
![home][home]  
Here is the form for inputting ingredients which redirects to a list of all ingredients in the database:  
![addIn][addIn]  
![allIn][allIn]  
Here is the method form where users can input the steps and time expected and once submitted are redirected to a different method page:  
![addMethod][addMethod]  
![allMethods][allMethods]  
Here is where users can put together a recipe that calls on an ingredient from the database as well as a method:   
![recipe][recipe]   
![edit_recipe][edit_recipe]  

#### **Known Issues**
There are a few problems with my current application:

* When the user inputs a recipe, they are only able to select one ingredient which is problematic when trying to follow. However, the method does include all of the ingredients but ideally you could clearly see a list of them.
* My integration test is not currently passing in all areas so I would like that working and passing in order to confirm my application is working as a whole.

### **Future Improvements**
There are a number of improvements I would like to implement:

* Fix the issue mentioned previously.
* Obtain a fully successful integration test.
* Allow people to specify cuisines so that users can get more information about a recipe they may not have seen before.
* Implement the option to include an image so that users can visulise the food.
* Improve the general look of my application with some colour.
* Get 100% test coverage so that there are no lines of code not accounted for.

### **Author**

Hannah Lister-Sims


[erd1]:https://i.imgur.com/ottJuBm.png
[erd2]:https://i.imgur.com/HTgA3Or.png
[erd]:https://i.imgur.com/lkntSuq.png
[CI_Pipeline]:https://i.imgur.com/7kNX2Zx.jpg
[Trello_board]:https://i.imgur.com/7n2wcRN.png
[risk_assessment]:https://i.imgur.com/xQtoidV.png
[test_cov]:https://i.imgur.com/yTyrg2x.png
[test_int]:https://i.imgur.com/6OTjQIH.png
[jenkins]:https://i.imgur.com/7sBfnL1.png
[home]:https://i.imgur.com/TgYwcL5.png
[addIn]:https://i.imgur.com/g9JUIlm.png
[allIn]:https://i.imgur.com/1CP1R7P.png
[addMethod]:https://i.imgur.com/8qtbEMk.png
[allMethods]:https://i.imgur.com/sazTkC1.png
[recipe]:https://i.imgur.com/MeJuMOC.png
[edit_recipe]:https://i.imgur.com/xc16vfz.png
