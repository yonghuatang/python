try:
    12/0
except ZeroDivisionError:
        print("IOP")

        
        

def derivatives(f,x,h=0.0001): # h has a default value
    df =(f(x+h) - f(x-h))/(2.0*h)
    ddf =(f(x+h) - 2.0*f(x) + f(x-h))/h**2
    return df,ddf
