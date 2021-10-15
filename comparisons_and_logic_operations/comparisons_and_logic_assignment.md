#+STARTUP: showall
#+OPTIONS: todo:nil tasks:nil tags:nil toc:nil
#+PROPERTY: header-args :eval never-export
#+EXCLUDE_TAGS: noexport
#+LATEX_HEADER: \usepackage{breakurl}
#+LATEX_HEADER: \usepackage{newuli}
#+LATEX_HEADER: \usepackage{uli-german-paragraphs}

** TODO

test that pdf field actually work



* Assignment 

\TextField[width=6cm,name=first]{First Name:}\\
\TextField[width=6cm,name=fam]{Family Name:}\\
\TextField[width=6cm,name=id]{Student ID:}\\

** Learning outcomes:

 - become familiar with reading comparison operators
 - become familiar with logic values
 - become familiar with logic operators


* Do not code!
Note that this part of the assignment should be done by hand, i.e.,
you should predict the results based on your understanding rather
than reporting the result of some code. It is easy to cheat on this one,
but if you are curious about how well you understand the material,
do this without the help of python. I will count on your honor and
curiosity. You can, however, use the pdf version of the textbook (or the
previous notebook link) to look up concepts (similar to an open book
exam).

You have two options to submit your assignment:

A) You can fill in the pdf form and print it as a pdf file. And then
   submit the printed pdf file on Quercus. This works on most
   operating systems.

B) Depending on your pdf viewer, you can fill out the pdf form and
   save it as "comparisons-FirstName-LastName.pdf" and submit this on
   Quercus. Test that your answers are indeed saved!

C) You can print the above assignment on paper and use a pencil to
   write down your questions and then use an app to convert it back to
   pdf format.
c
   \begin{itemize}

   \item Android: https://www.howtogeek.com/249200/how-to-combine-multiple-images-into-a-pdf-file-on-android/

   \item IPhone: https://pdf.wondershare.com/mobile-app/free-photo-to-pdf-app.html
   \end{itemize}


1. The results of comparisons are reported as the logical (boolean)
   values of either =True=, or =False=. Does the truth value equal
   \TextField[width=4cm,name=1]{one or zero?} (1pt) 
   
2. How does your notebook indicate that =True=
   \TextField[width=4cm,name=2]{has a special meaning?} (1pt)

3.Let a be equal to 12, and b be equal to 12.0, will the following comparison result in a True or False value?
     \TextField[width=4cm,name=3]{ a == b } (1pt)

4. [@4] Edit the following lines and add the boolean value (i.e.,
   True/False or error) for each statement.(11 pts)
     \begin{itemize}
     \item \TextField[width=4cm,name=f1]{  True > False }
     \item \TextField[width=4cm,name=f2]{ 5 == 4  }
     \item \TextField[width=4cm,name=f3]{  2 != 3  }
     \item \TextField[width=4cm,name=f4]{  5 > 4  }
     \item \TextField[width=4cm,name=f5]{  5 < 4  }
     \item \TextField[width=4cm,name=f6]{  1 >= 1 }
     \item \TextField[width=4cm,name=f7]{  2 <= 2 }
     \item \TextField[width=4cm,name=f8]{ -12 <= -4 }
     \item \TextField[width=4cm,name=f9]{ True == True }
     \item \TextField[width=4cm,name=f10]{ True != False }
     \item \TextField[width=4cm,name=f11]{ True != true  }
     
    \end{itemize}
  
5. Edit the following lines and add the boolean value (i.e.,
   True/False) for each statement.  (11 pts).
     \begin{itemize}
     \item \TextField[width=4cm,name=v1]{ (True and True) or False }
     \item \TextField[width=4cm,name=v2]{ True and True }
     \item \TextField[width=4cm,name=v3]{ True and False }
     \item \TextField[width=4cm,name=v4]{ False and False }
     \item \TextField[width=4cm,name=v5]{ False or True }
     \item \TextField[width=4cm,name=v6]{ True or False }
     \item \TextField[width=4cm,name=v7]{ not(True) or not(False) }
     \item \TextField[width=4cm,name=v8]{ not(True or False) }
     \item \TextField[width=4cm,name=v9]{ not(True) and not(False) }
     \item \TextField[width=4cm,name=v10]{ not(True and False) }
     \item \TextField[width=4cm,name=v11]{ not(True and False) or True }
     
    \end{itemize}

6. Edit the following lines and add the result for each statement.  (10 pts).
     \begin{itemize}
     \item \TextField[width=4cm,name=v1]{ a = 5}
     \item \TextField[width=4cm,name=v2]{ b = 12}
     \item \TextField[width=4cm,name=v3]{ not(a < 0 and b > 0) }
     \item \TextField[width=4cm,name=v4]{ a > 0 and b > 0}
     \item \TextField[width=4cm,name=v5]{ a < 0 and b > 0 }
     \item \TextField[width=4cm,name=v6]{ a < 0 or  b > 0 }
     \item \TextField[width=4cm,name=v7]{ a < 0 or  b < 0  }
     \item \TextField[width=4cm,name=v8]{ not(a < 0) and  b > 0}
     \item \TextField[width=4cm,name=v8]{ not(a < 0) or   b > 0}
     \item \TextField[width=4cm,name=v9]{ not(a < 0 or b > 0) }
   
    \end{itemize}
#   \end{Form}

8. [@8] 2pts. You have the following python dictionary: 
#+BEGIN_SRC ipython
d = {"Apples":10, "Oranges":12}
#+END_SRC
Write a one-line python statement that yields =True= if there are more than eight apples in the dictionary.

\TextField[width=8cm,name=8]{}

9. [@9] 2pts
You have the following python dictionary: 
#+BEGIN_SRC ipython
d = {"Apples":10, "Oranges":12}
#+END_SRC
Write a one-line python statement which yields =True= if there are more than eight apples and less than 12 Oranges in the dictionary.

\TextField[width=8cm, name=9]{}

Total points: 39
