def add(someString):

   stringLength = len(someString)
   getDelimeter = ""
   for i in range(2,stringLength):
       if someString[i] != "\n":
           getDelimeter += someString[i]
       else:
           break
   
   someString = someString.split(getDelimeter)
   addNumber = 0
   for i in someString:
       if i != "//" and i != " ":
           addNumber += int(i)
   print(addNumber)

add("//;;\n11;;22")
