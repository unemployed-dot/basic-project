"""
Created on Wed Oct  9 14:58:54 2019

@author: Unemployed

"""

import random

chars='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
password=''

#The program permits to generate a file in which saves passowrds and sites. 

site=input('For which site do you need the password ')
username=input('Insert usarname ')
lenght=int(input('Enter the password length '))

for i in range(lenght):
    password=password+random.choice(chars)

file1=open('Saved Password.txt','a')
file1.write('\n'+site +'       '+ username+ '         ' + password)    
file1.close()
