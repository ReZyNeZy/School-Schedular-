# Python School Calendar w Grade Calculator 

## Overview

This application is a website that allows users to create a calendar of their classes. Users can also calculate their final grades for a class by inputting the weight of a particular grade, and the overall grade in that particular section of the class. User have the option of saving their grades to a separate list from the school schedule for easy access to grades. This program makes use of a simple CRUD menu to add, delete, edit, and view the schedule entries users insert. Users have the option to include a time, class name, location, and days the class is in session. The information of grades and class schedue is displayed via a CSS grid to present the information in a clean and clear manner. There is also a username and password function that makes use of cookies. 

Both the grade calculator and class schedule make use of the the SQLite lbrary provided by Python3. SQLite is prefferred as it is simpler than SQL while still maintaining most of the features of SLQ. The web framework is provided by bottle. Bottle is a simple framework and only requires the standard python library in order to route and post webpages. Python is used sporatially for calculations, and SQLite implementation directly in the html files used. Python also provides bottle with its ablilities as a web framework. 

In the futurure I hope to iron out the username and password function. Currently there is only one user allowed in the system and that information is stored directly in file rather than encrypted and stored in a seprarate location. This poses a major security risk and makes the use of cookies redundant. There is also an uneccesarry separation of the login page from the main menu. This page only exists to make the cookies justified and should be removed in later updates. THe page is also very bland and could use some JavaScript to beautify the work. CSS and APIs could also seek to make the page easier on the eyes.

## Installation and Runtime

This file was created using pythonanywhere. Pythonanywhere provides free webhosting for 6 months and makes use of easy separation of of files. PythonAnywhere also provides a multitude of frameworks to manage your website. If you wish to host this program using python anywhere, a link to their site can be found [Here]{https://www.pythonanywhere.com}.

While many frameworks exist to route sites, this program was designed with the framework of bottle. It is reccomended that this program be continued to run in bottle. If you wish to use a diffrent framework, it may be required to reformat files included. 

To run the program. locate the file titled 
      bottle_app.py. 
