# Hassham Malik
# Assignment 10.1: Your Own Class
# The purpose of this scrpit is to implement my own class based on a real-world object.
# Along with a short demo program in the main function that highlights all my class variables and methods

class Students:
    # class variable
    student_count = 0

    # initializing data members
    def __init__(info, ID, name, grade):
        info.__ID = ID
        info.__name = name
        info.__grade = grade
        Students.student_count += 1

    # the following method gets the ID
    def get_ID(info):
        return info.__ID

    # the following method gets the name
    def get_name(info):
        return info.__name
    
    # the following method gets the grade
    def get_grade(info):
        return info.__grade
    
    # the following method sets the ID
    def set_ID(info, ID):
        info.__ID = ID
    
    # the following method sets the name
    def set_name(info, name):
        info.__name = name
    
    # the following method sets the grade
    def set_grade(info, grade):
        info.__grade = grade
    
    # method for displaying information about the object which is a Student
    def display(info):
        print("Student ID:", info.get_ID())
        print("Student Name:", info.get_name())
        print("Student Year:", info.get_grade())

    # method for printing total number of students
    def print_total_students(info):
        print("The total number of students is", Students.student_count)

# main funciton
def main():

    # creating objects
    s1 = Students(1357, 'Hassham', 'Junior')
    s2 = Students(2468, 'Muhammad', 'Sophmore')
    s3 = Students(3579, 'Adam', "Freshman")
    s4 = Students(4680, 'Humza', 'Senior')

    # printing ID of s1 using the getter method
    print("Student ID of s1:", s1.get_ID())

    # setting ID of s1 using setter mehtod
    s1.set_ID(1234)

    # printing the ID of s1 again using getter method
    print("Student ID of s1:", s1.get_ID())

    # printing all information about student s1
    print("\n~*~*~ Info of s1 ~*~*~")
    s1.display()
    print()

    # printing total number of students
    s1.print_total_students()

main()