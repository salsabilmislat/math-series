


def fibonacci(n):
    """
    this function should return the nth value in the fibonacci series.
    """
   
    if n==0:
       return 0

    if n==1:
       return 1
    
    return fibonacci(n-1) + fibonacci(n-2)
    
  
    

  



def lucas(n):
    """
    this function should returns the nth value in the lucas numbers
    
    """

    if n==0:
       return 2

    if n==1:
       return 1

    return  lucas(n-1) +  lucas(n-2)


def sum_series(n,n1=0,n2=1):

    """
    this function it is taking an input and return your own series if you put any number that you want to start that series for
    
    """
    if n==0:
       return n1

    if n==1:
       return n2

    return sum_series((n-1),n1,n2) + sum_series((n-2),n1,n2)