from bottle import route,  template, post



import sqlite3


contactSchedDB = sqlite3.connect("./mysite/views/Schedule.db")

contactSchedule = contactSchedDB.cursor()


contactGradesDB = sqlite3.connect("/home/ajmacken/mysite/views/Grades.db")

contactGrades = contactGradesDB.cursor()

@route('/schedlog')

def schedlog():

    return template('schedLogin.html')

@route('/mainPage')

def mainPage():

    return template('mainPage.html')

@route('/weightgrades')

def weightedCalculate():

    return template('weightedCalculate.html')

@route('/schedit')

def scheduleEdit():

    return template('edit_sched.html')


@post('/resultWeighted')

def weightedResults():

    return template('weightedResult.html')

@post('/saveGrades')

def saveGrades():

#add sql once working

    return template('saveGrades.html')

@route('/viewSched')

def viewSched():

    return template('viewSched.html', c = contactSchedule)

@route('/viewGrades')

def viewGrades():

    return template('viewGrades.html' , c = contactGrades)

@route('/addToSched')

def addToSched():

    return template('addToSched.html')

@post('/addToSchedB')

def addToSchedB():

    return template('addToSchedB.html' , c = contactSchedule , db = contactSchedDB)

@post('/saveGradesB')

def saveGradesB():

    return template('saveGradesB.html' , c = contactGrades, db = contactGradesDB)

@route('/deleteGrade')

def deleteGrade():

    return template('deleteGrade.html' , c = contactGrades)

@post('/confirmGrades')

def confirmGrades():

    return template('confirmGrades.html', c= contactGrades)

@route('/removeEntry')

def deleteClass():

    return template('removeClass.html' , c = contactSchedule)

@post('/confirmDelete')

def confirm():

    return template('Confirm.html', c = contactSchedule)

@post('/deleteGradeB')

def deleteGradesB():

    return template('deleteGradeB.html', c = contactGrades, db= contactGradesDB)


@post('/removeClassB')

def removeB():

    return template('removeClassB.html', c = contactSchedule, db = contactSchedDB)

@route('/editEntry')

def editEntry():

    return template('editEntry.html' , c = contactSchedule)

@post('/editEntryB')

def editB():

    return template('editEntryB.html', c = contactSchedule)

@post('/editEntryC')

def editC():

    return template('editEntryC.html', c = contactSchedule, db = contactSchedDB)

@route('/login')

def login():

    return template('finalLogin.html')

@post('/loginTest')

def loginTest():

    return template('finalLoginB.html')

@route('/schedStart')

def start():

    return template('startPage.html')

@route('/loginC')

def loginC():

    return template('loginC.html')

@route('/logout')

def logout():

    return template('logOut.html')





