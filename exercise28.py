Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> True and True
True
>>> False and True
False
>>> 1==1 and 2==1
False
>>> "test" == "test"
True
>>> 1 == 1 or 2!=1
True
>>> True and 1 == 1
True
>>> False and 0!=0
False
>>> True or 1 == 1
True
>>> "test" == "testing"
False
>>> 1!=0 and 2==1
False
>>> "test" != "testing"
True
>>> "test" == 1
False
>>> not(True and False)
True
>>> not (TRUE AND FALSE)  #Tried to use CAPS and see the output.
  File "<stdin>", line 1
    not (TRUE AND FALSE)
              ^
SyntaxError: invalid syntax
>>> not(1==1 and 0!=1)
False
>>> not(10==1 or 1000==1000)
False
>>> not(1!=10 or 3==4)
False
>>> not("testing"=="testing" and "Zed" == "Cool Guy")
True
>>> 1 == 1 and (not("testing"==1 or 1==0))
True
>>> "chunky"=="bacon" and (not(3==4 or 3==3))
False
>>> 3==3 and (not("testing" == "testing" or "Python" == "Fun"))
False
