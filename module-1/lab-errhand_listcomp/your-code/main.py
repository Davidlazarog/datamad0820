'''#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)
'''
#Insert here the module/library import statements 

import random as rd
import os 
import sys

#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square = [i**2 for i in range(0,20)]
print(square)



#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two = [2**i for i in range(0,50)]
print(power_of_two)




#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt = [i**0.5 for i in range(0,100)]
print(sqrt)




#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

my_list = [i for i in range(-10,1)]




#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odd = [i for i in range(1,101) if i % 2 == 0]
print(odd)



#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven = [i for i in range(1,101) if i % 7 == 0]
print (divisible_by_seven)



#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Travesura realizada'
vowels = [ "a" , "e" , "i" , "o" , "u" ] 
non_vowels = ''.join([x for x in teststring if x not in vowels])
print(non_vowels)




#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

testString2 = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters = ''.join([i for i in testString2 if  i.isupper()])
print(capital_letters)




#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

teststring = 'The quick brown fox jumped over the lazy dog'
consonantes = list("bcdfghjklmnpqrstvwexyz")
consonants = ''.join([x for x in teststring if x.lower() not in consonantes])
print(consonants)



#10. Find the folders you have in your madrid-oct-2020 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

files = [x for x in os.listdir("/Users/david/IRONHACK/datamad0820")]
print(files)




#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

import random as rd
random_lists = [[rd.randrange(0,100) for i in range(11)],[rd.randrange(0,100) for i in range(11)],[rd.randrange(0,100) for i in range(11)] ,[rd.randrange(0,100) for i in range(11)]]

print(random_lists)


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list =[e for x in list_of_lists for e in x]
print(flatten_list)



#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats = [float(e) for i in list_of_lists for e in i]
print(floats)



#14. Handle the exception thrown by the code below by using try and except blocks. 

try:
    for i in ["a","b","c"]:
        print(i**2)
except TypeError:
    print("El tipo es equivocado")
except SyntaxError:
    print("Sintaxis equivocada")


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0

try:
   z = x/y 
except ZeroDivisionError:
    print("No puedes dividir entre cero")
finally:
    print("All Done")


#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]
try:
    print(abc[3])
except IndexError:
    print("No puedes poner eso")


#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 


#He recibido ayuda en este porque no lo entiendo. Y creo que sigo sin entenderlo. 
try:
    f = open('testfile','r')
    f.write('Test write this')
except Exception as e:
    print("Eso no se puede escribir")




#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())
except FileNotFoundError:
    print("No existe ese archivo")
except NameError:
    print("El nombre no es correcto")
except ValueError:
    print("No me cuadra ese valor amigo")



#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    try:
        assert ('linux' in sys.platform), "Function can only run on Linux systems."
    except Exception as e:
        print('Function can only run in Linux sistem')
    print('Doing something.')


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.

'''
def integrer ()
    numero = input("Dime un numero")
    return(f'El cuadrado de tu numero es {numero**2}')

while True:
    integer()
        break
except Exception as e
    print("Algo ha fallado")
    print (e)
    print ("intentelo de nuevo")
    integer()
finally:
    print("conseguido")



'''
# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

result=[]
for j in range(1,1000):
    for x in range(2,10):
        if j % x == 0:
            result.append(x)
print(result)

'''
# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python



#Esto me da error y no entiendo por qué, por mas que busco en internet la sintaxis esta bien y me devuelve ese error
class Num_of_sections_Error[Exception]:
    pass

try:
total_marks = int(input("Enter Total Marks Scored: ")) 
num_of_sections = int(input("Enter Num of Sections: "))
    if(num_of_sections < 2):
        raise Num_of_sections_Error
except Num_of_sections_Error:
    print("El numero de secciones tiene que ser mayor que dos")


'''
