#BugReport-Lab_CaseStudyM02

** Preconditions **

- Line 20

**Steps to Reproduce**

- Print the list of vehicle details


**Expected Results**

- Please enter the type of vehicle : car
Enter the year of the vehicle : 2017
Enter the make of the vehicle : buick
Enter the model of the vehicle :regal gs
Enter number of doors : 4
Enter type of roof (solid or sun roof) :sun roof
('Vehicle type: car', 'Year: 2017', 'Make: buick', 'Model: regal gs', 'Number of doors: 4', 'Type of roof: sun roof')

**Actual Results**

details = ("Vehicle type: " + Type
               ^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?


**FIX**

- Inserted commas between the listed items on lines (20-25)

details = ("Vehicle type: " + Type, 
    "Year: " + Year, 
    "Make: " + Make, 
    "Model: " + Model, 
    "Number of doors: " + Doors, 
    "Type of roof: " + Roof)