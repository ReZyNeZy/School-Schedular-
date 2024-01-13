# Python School Calendar w Grade Calculator 

## Overview

This application is a website that allows users to create a calendar of their classes. Users can also calculate their final grades for a class by inputting the weight of a particular grade, and the overall grade in that particular section of the class. User have the option of saving their grades to a separate list from the school schedule for easy access to grades. This program makes use of a simple CRUD menu to add, delete, edit, and view the schedule entries users insert. Users have the option to include a time, class name, location, and days the class is in session. The information of grades and class schedue is displayed via a CSS grid to present the information in a clean and clear manner. There is also a username and password function that makes use of cookies. 

Both the grade calculator and class schedule make use of the the SQLite lbrary provided by Python3. SQLite is prefferred as it is simpler than SQL while still maintaining most of the features of SLQ. The web framework is provided by bottle. Bottle is a simple framework and only requires the standard python library in order to route and post webpages. Python is used sporatially for calculations, and SQLite implementation directly in the html files used. Python also provides bottle with its ablilities as a web framework. 

In the futurure I hope to iron out the username and password function. Currently there is only one user allowed in the system and that information is stored directly in file rather than encrypted and stored in a seprarate location. This poses a major security risk and makes the use of cookies redundant. There is also an uneccesarry separation of the login page from the main menu. This page only exists to make the cookies justified and should be removed in later updates. THe page is also very bland and could use some JavaScript to beautify the work. CSS and APIs could also seek to make the page easier on the eyes.

## Installation and Runtime

This file was created using pythonanywhere. Pythonanywhere provides free webhosting for 6 months and makes use of easy separation of of files. PythonAnywhere also provides a multitude of frameworks to manage your website. If you wish to host this program using python anywhere, a link to their site can be found [Here]{https://www.pythonanywhere.com}.

While many frameworks exist to route sites, this program was designed with the framework of bottle. It is reccomended that this program be continued to run in bottle. If you wish to use a diffrent framework, it may be required to reformat files included. 

Some setup is required if using pythonanywhere. Simply navigate to the web tab and set up your website. Select the bottle framework, or whatever framework you want to use. Your webpage will be allocated to you for 6 months before a refresh of the website is required.

To run the program. locate the file titled 

      bottle_app.py


 execute this file to start your website. 


## How to Use

### Login

The bottle app file should show you which routes the program contains. Locate the login route and add this to the end of your url. The program will ask for a login. 

      user: demo
      pass: final

 Cookies will work to chech if the username and password is correct. If correct, the page will prompt you to click a button to take you to the main menu. If false, the user will be prompted to return to the login page. 

### Main Menu

 Upon entering the menu. There should be options to 

 1. Log out
 2. View Grades
 3. View Schedule
 4. Calculate Grades

### Grade Calculator

The Grade Calculator is used for calculating weighted grades. Input the grade catagories and assign them a weight. The program will calculate your final grades using simple math. Users can then choose to save these grades or delete them. If you save the grades, they automatically are put into the list of grades accessable throught the main menu.

### Schedule Menu

Upon accessing the schedule menu, users are prompted with a CRUD menu. Users can create new entries, edit existing entries, delete entries, and view entries as well as return to the main menu page.




