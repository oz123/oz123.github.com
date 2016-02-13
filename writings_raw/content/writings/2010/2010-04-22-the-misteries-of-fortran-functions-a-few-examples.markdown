---
title: The misteries of Fortran Functions 
author: Oz Nahum
published: 2010-04-22
tags: Programming, Fortran
public: yes
chronological : yes
kind: writing 
summary: Fortran has a 2 ways to define sub-procedures: functions and subroutines. Functions allow many input variables, but only one output variable, which has to be a number. Subroutines, can take a few variables and output a few variables.
---

Fortran has a 2 ways to define sub-procedures: functions and subroutines. Functions allow many input variables, but only one output variable, which has to be a number. Subroutines, can take a few variables and output a few variables.
At first glance, this separation looks unnecessary, but it helps you keep your code easy to understand, provided you use functions. In the following a I give a few examples of how I found I can use functions in Fortran:



    
    
    PROGRAM function_demo1
    ! *** Program to demonstrate a function
    IMPLICIT NONE
    REAL :: a,b,c ! *** Declare a,b,c
    PRINT*,"Enter number one"
    READ*,a
    PRINT*,"Enter number two"
    READ*,b
    c=calc(a,b)
    PRINT '("Answer = ",f10.4)',c
    CONTAINS
    !
    FUNCTION calc(d,e)
    REAL :: d,e
    REAL :: calc
    ! *** Dummy variables
    ! *** Local Variables
    calc=SQRT(d**2+e**2)
    END FUNCTION calc
    END PROGRAM function_demo1
    


Notice the word  "CONTAINS" above.

    
    
    PROGRAM function_demo2
    ! *** Program to demonstrate a function
    IMPLICIT NONE
    !External Function declaration
    REAL, EXTERNAL :: calc
    REAL :: a,b,c ! *** Declare a,b,c
    PRINT*,"Enter number one"
    READ*,a
    PRINT*,"Enter number two"
    READ*,b
    c=calc(a,b)
    PRINT '("Answer = ",f10.4)',c
    END PROGRAM function_demo2
    !
    REAL FUNCTION calc(d,e)
    IMPLICIT NONE
    REAL :: d,e  ! *** Dummy variables
    !REAL :: calc !  *** Local Variables
    calc=SQRT(d**2+e**2)
    END FUNCTION calc
    



The third way will be:

    
    
    PROGRAM function_demo3
    ! *** Program to demonstrate a function
    IMPLICIT NONE
    !External Function declaration
    REAL, EXTERNAL :: calc
    REAL :: a,b,c ! *** Declare a,b,c
    PRINT*,"Enter number one"
    READ*,a
    PRINT*,"Enter number two"
    READ*,b
    c=calc(a,b)
    PRINT '("Answer = ",f10.4)',c
    END PROGRAM fuction_deom3
    !
    REAL FUNCTION calc(d,e) RESULT (CR)
    IMPLICIT NONE
    REAL :: d,e  ! *** Dummy variables
    !REAL :: calc !  *** Local Variables
    CR=SQRT(d**2+e**2)
    END FUNCTION calc
    



And there is even a forth way !


    
    
    PROGRAM function2
    ! *** Program to demonstrate a function
            IMPLICIT NONE
            !External Function declaration
            REAL, EXTERNAL :: calc
            REAL :: a,b,c ! *** Declare a,b,c
            PRINT*,"Enter number one"
            READ*,a
            PRINT*,"Enter number two"
            READ*,b
            c=calc(a,b)
            PRINT '("Answer = ",f10.4)',c
    END PROGRAM function2
            !
            !REAL FUNCTION calc(d,e)
    FUNCTION calc(d,e)
           IMPLICIT NONE
            REAL :: d,e  ! *** Dummy variables
            REAL :: calc !  *** Local Variables
           calc=SQRT(d**2+e**2)
    END FUNCTION calc
    
    


Notice that the return value of the function has a different name from the function name. All these programs compile equally under gfortran 4.3 in Debian Squeeze.
