# Assignment 10.1
Part 1:
The following class is called Students and the purpose of this class is to be able to take in objects, in this case the objects are Students. We will be using those objects to get informaiton about the Students for example their names and ID numbers.
To start off, there is one class variable and it is called student_count this variable is pretty self explanitory as it is responsible for keeping track for the number of objects (Students) that are being assigned.
There are three data variables, first one is called ID which stores the ID number of the student.
The second data variable is called name which stores the name of the student.
The final data variable is called grade which stores the students current grade level.
There are quite a few methods in this class and I will describe every single one, starting with the __init__ method. This method is very important as it is responsible for initializing all the data variables that we are taking in from all the objects that we pass into the class. At the end of this method there is a line of code that increments our class variable by 1, which is important because it helps us keep count of the total number of obejects (Students).
The seccond method is called get_ID, this method is a getter method which takes in a specified object and returns the ID number of it.
The third method is called get_name, this method is a getter method which takes in a specified object and returns the name of it.
The fourth method is called get_grade, this method is a getter method which takes in a specified object and returns the grade level of it.
The fifth method is called set_ID, this method is a setter method which takes in a specified object and sets the ID number to whatever it is asked to do through main.
The sixth method is called set_name, this method is a setter method which takes in a specified object and sets the name to whatever it is asked to do through main.
The seventh method is called set_grade, this method is a setter method which takes in a specified object and sets the grade to whatever it is asked to do through main.
The eighth method is called display, this method is displays all the information about the specified object. It starts off by printing a header line, then follows with the Student ID, then the name, and finally the grade, all on different lines.
The ninth and final method is called print_total_students which brings our class variable into play and prints out the total number of objects (Students) that were created in main.

Part 2:
The demo program can be found in the main function. First thing that we do in the demo program is create all the objects, each object is given a name that we use throughout the main funciton, but it comes with the following values stored: ID number, name, and grade. At first we test our getter method to make sure it is funcitoning properly, then we use the setter method, follwed by the getter method again to make sure that we were able to change the value that we wanted through the setter method. After all that is done then we test the last two other methods by first displaying all the infotmation for one of our objects. Then we finally test our final method which will print the total number of objects (Students). The way that the user can run this demo program is to simply compile this program because I have already set it to run the main method, which contains the Demo Program which tests every method.
