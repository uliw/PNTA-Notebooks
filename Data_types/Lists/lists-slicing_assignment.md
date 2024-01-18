

# Assignment

Note: It may be easiest if you copy this entire notebook to your
submission folder and add title and id etc. rather than the other way
round. 

Adding information is easily done by splitting an existing text cell
into two cells. After copying this notebook, click on this text cell
and place the cursor after the last sentence. Now select Edit-> Split
Cell (or hit `Ctrl-Shift-Minus`).


## Learning Outcomes

-   Learn how to split a text cell into two
-   Create lists
-   Access list elements
-   Get comfortable selecting subsets from list-type variables using
    slicing syntax


## Here be dragons!

Within your notebook all variables are shared. Imagine the following: You start your assignment with
the following two code blocks

    a = [1, 2, 3, 4]

    print(sum(a))

and further down you have a statement like `a = [-2, 3]` . As it happens, you return to the beginning of your notebook, and execute the second code cell, but this time the sum will not be 10 but 1, because the value of a is now  `[-2, 3]`, and no longer `[1, 2, 3, 4]`

There are two strategies to avoid this problem:

-   Always run all cells in the notebook (select Run-> Run all Cells from the menu)
-   Always declare the variables in the same code-cell you are using them.


## Questions 16 pts

Execute the following block so that `my_list` becomes known in your
local Jupyter session.

    my_list = [3, 4, 5, 12, 0, 11, 1, 2, 9, 8, 7, 13, 10]

Add a textbox here, and explain why the above statement does not
produce any output. 2 pts

Write a python statement that prints the last four elements of
`my_list` 1pt

    # Add your code here

Write a python statement that shows every 3rd element of `my_list`
starting with the third element in `my_list`. 2 pts

    # Add your code here

Write a python statement that shows every second element of the last 6
elements in `my_list` (2 pts). Note, consider splitting this into two
steps: 1) Where you first select the last six elements and save them
into a new list; 2) Then write a statement that selects every second
element. You can also chain list-slicing commands, e.g.,
`my_list[1:4][::2]`. In this case, you first specify a list from index
1 to 4, and then select every second element. Note that the expected
answer starts with the number 9. (2 pst)

    # Add your code here

Write a python statement that shows every second element of the last
six elements in `my_list` in reverse order. So if you have the following list, e.g., `[0, 2, 5 , 3, 12, 8, 3 - 2, 0]`, the last 6 elements would be `[3, 12, 8, 3 - 2, 0]`, every second element would be `[12, 3, 0]` and in reverse order you would get `[0, 3, 12]` . Chain your slicing
statements as in the example above. (3 pts)

    # Add your code here

What is the shortest slicing notation to show all values of `my_list` in reverse order? 2 pts

    # Add your code here

Add a textbox below, and explain why the next two
statements do not produce the same result 2 pts

    print(my_list[0:])
    print(my_list[0:-1])

What is wrong with this python statement below? 1 pt

    my_list = [1 2 3]

Add a python statement below That shows the first three words of `ml` (1 pt)

    ml = ["This", "is", "a", "short", "sentence"]


### Advanced questions (10 pts)


#### 1

Add a python statement that will use chained slicing syntax to extract the
first and the last element of the first list in the list of lists. Assume that the sub-list length is 3. (3 pts)

    ml = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


#### 2

Given a list of numbers `a`, write a function that returns the sum of every third number, starting from the second number, up to the second-to-last number (e.g., excluding both ends in `a`). For example, given the list \`a = [1, 2, 3, 4, 5, 6, 7, 8, 9]\`, the function should return the sum \`2 + 5 + 8 = 15\`. Make sure to handle cases where the list has less than three numbers

Notes: You can calculate the sum of a list as

    a = [1, 2, 4]
    sum(a)

I recommend to first solve the problem of getting the correct list elements, and to copy these into a new list. The calculate the sum in a second step.

Test your code with the following lists (4 pts)

    my_list_1 = [15, 23, 83, 65, 37, 49, 35, 29, 97, 21, -12]
    my_list_2 = [2, -4]


#### 3

The following code, declares a list made up of lists. Write one-line python statement that extracts the second to forth element of the second list (3 pts)

    mll = [
        [1, 2, 4, 5],
        [83, 65, 37, 49, -100],
        [29, 97, 21, -12],
    ]


## Marking Scheme

Total points: 30

-   24 pts for the questions
-   2 pts for correct notebook formatting
-   2 pts for correct notebook name


## Submission Instructions

Create a new (or copy and existing) notebook in your `submissions`
folder before editing it. Otherwise, your edits may be overwritten the
next time you log into syzygy. Please name your copy `assignment-name-firstname-lastname` 

-   Replace the `assignment-name` with the name of the assignment
    (i.e., the filename of the respective Jupyter Notebook)
-   `firstname-lastname` with your own name.

Note: If the notebook contains images, you must also copy the image files!

Your notebook/pdf must start with the following lines :

**ESS245: Assignment Title**

**Date:**

**First Name:**

**Last Name:**

**Student: Id**

Before submitting your assignment:

-   Check the marking scheme and ensure you have covered all requirements.
-   Re-read the learning outcomes and verify that you are comfortable
    with each concept. If not, please speak up on the discussion board
    and ask for further clarification. I can guarantee that if you feel
    uncertain about a concept, at least half the class will be in the
    same boat. So don't be shy!

To submit your assignment, you need to download it as `ipynb` notebook
format **and** `pdf` format. **To export your notebook as pdf
use your browser's print function (`Ctrl-P`) and then select**
`Save as pdf`.  In the past, this worked best with Chrome or Firefox.

 Please submit **both files** on Quercus. Note that the pdf
export can fail if your file contains invalid markup/python code. So
you need to check that the pdf export is complete and does not miss
any sections. If you have export problems, don't hesitate to contact
the course instructor directly.

Notebooks typically have empty code cells in which you must enter
python code. Please use the respective cell below each question, or
create a python cell where necessary. Add text cells to enter your
answers where appropriate. Your responses will only count if the code
executes without error. It is thus recommended to run your solutions
before submitting the assignment.

**Note: Unless specifically requested, do not type your answers by**
**hand. Instead, write code that produces the answer. Your pdf file**
**should show the code and the results of the code execution.**

