#!/bin/bash

#Ejercicio 1
echo "Hello World"
#Ejercicio 2
mkdir "new_dir"
#Ejercicio 3
rm -r "new_dir"
#Ejercicio 4
cp lorem/sed.txt lorem-copy/
#Ejercicio 5 
cp lorem/at.txt lorem-copy/ ; cp lorem/lorem.txt lorem-copy/
#Ejercicio 6 
cat lorem/sed.txt
#Ejercicio 7
cat lorem/at.txt ; cat lorem/lorem.txt
#Ejercicio 8 
cat lorem-copy/sed.txt| head -n 3
#Ejercicio 9 
cat lorem-copy/sed.txt| tail -n 3
#Ejercicio 10
echo -e "Homo Homini Lupus" >> lorem-copy/sed.txt
#Ejericio 11
cat lorem-copy/sed.txt| tail -n 3
#Ejercicio 12
sed "s/et/ET/g" lorem-copy/at.txt
#Ejericcio 13
whoami
#Ejercicio 14
pwd
#Ejercicio 15 
ls lorem/*.txt
#Ejercicio 16
wc -l lorem/sed.txt
#Ejercicio 17 
ls -f | grep -c "^lorem"
#Ejercicio 18 
grep 'et' lorem/at.txt
#Ejercicio 19 
grep -c 'et' lorem/at.txt
#Ejercicio 20 
grep -r 'et' lorem-copy/ | wc -l




### BONUS ###

#Ejercicio 21
name="David"
#Ejercicio 22
echo $name
#Ejercicio 23
mkdir $name
#Ejercicio 24
rmdir $name
#Ejercicio 25 
#25.1 
for file in $(ls lorem/):
for> echo item $file
#25.2
for file in $(ls lorem/):      
for> echo item $#file
#25.3
for file in $(ls lorem/):
for> printf "%s has %s characters length\n" "$file" "${#file}" 

# he recibido ayuda aqui, se que no se puede pero casi puede conmigo. 
# no entiendo porque no funciona asi, si deberia de ser lo mismo. 
# printf "("$file" has "${#file}" characters length\n")

#Ejercicio 26 
top
#Ejercicio 27 