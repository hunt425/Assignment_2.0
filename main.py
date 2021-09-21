########################################################################
##
## CS 101 Lab
## Program #
## Hunter Tysdal
## htt4kk@umsystem.edu
##
## PROBLEM : Figuring lab grade with grade weights
##
## ALGORITHM :

print('**** Welcome to the LAB grade calculator! ****')

name = input('Who are we calculatiung grades for? ==> ') #ask for name

labs = int(input('Enter Labs grade ==> '))
if labs > 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    lab = 100
elif labs < 0:
    print('The lab value should have been zero or greater. It has been changed to zero')
    labs = 0

exams = int(input('Enter the EXAMS grade ==> '))
if exams > 100:
    print('The exam value should have been 100 or less. It has been changed to 100.')
    exams = 100
elif exams < 0:
    print('The exam value should have been zero or greater. It has been changed to zero')
    exams = 0

attendance = int(input('Enter the Attendance grade ==> '))
if attendance > 100:
    print('The attendance value should have been 100 or less. It has been changed to 100.')
    attendance = 100
elif attendance < 0:
    print('The attendance value should have been zero or greater. It has been changed to zero')
    attendance = 0

labs = (labs / 100) * 7
exams = (exams / 100) * 2
attendance = (attendance / 100) * 1



total = (labs + exams + attendance) * 10
print('The weighted grade for {} is {:.1f}'.format(name, total))

grade = 'A'
if total >= 90 and total < 100:
    grade = 'A'
elif total >= 80 and total < 90:
    grade = 'B'
elif total >= 70 and total <80:
    grade = 'C'
elif total >= 60 and total < 70:
    grade = 'D'
elif total >=0 and total < 60:
    grade = 'F'

print('{} has a letter grade of {}'.format(name, grade))
print()
print('**** Thanks for using the Lab grade calculator ****')