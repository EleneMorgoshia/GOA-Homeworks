print("this is a lesson 2 ") 
 
#GROUP 102
#string and its abilities

# #for short strings
name="elene" 

# #length of the variable
print(len(name)) #len-(length) of the variable 

#------------------------------

# #for  longer  strings- use """.........."""
my_sentence="""Hello,first lesson will be held
# in 19 september,
# pls do not be late""" 
print(my_sentence)

#--------------------------------
knows_programing=True

if True:
    print("hello") #indentation by using tab

#-------------------------------

full_name="Elene Morgoshia" #5+1(space)+9=15
print(len(full_name))

#every string should be realised as a list
print(full_name[0]) #the first index
print(full_name[6]) #do not forget the space!


#------------------------------
# #how to print the letter from  string
full_name="Elene Morgoshia"
print("l"in full_name) 
print("M"not in full_name) 

#--------------------------------

#how to slice strings
full_name="Elene Morgoshia"
print(full_name[2:9]) #starting  with 2 and ending  with 8
# print(full_name[2:9:2]) #guideline of skiiping letters: #start:finish:step
print(full_name[0:15]) 
print(full_name[:6]) 

# ----------------------------------
#printing the negative index

full_name="Elene Morgoshia"
print(full_name[-1]) #[-1]-printing the last letter
print(full_name[-4]) # s
print(full_name[-4]+"abc")
print(full_name[-1:-6:-2])

# ---------------------------------------
#methods of string 
# 1)string.upper()
# 2)len(string)

full_name="Elene Morgoshia"
print(full_name.upper()) #incrreasing the letters
full_name2="ELENE MORGOSHIA"
print(full_name2.lower())

# STRIP
full_name3="  ELENE    "
print(full_name3.strip()) #cutting the space
 
#REPLACE (1)Something that will be changed 2)New variable )
print(full_name2.replace(" ","#")) 
print(full_name2.replace("E","#"))

#-----------------------------------------
# REVIEW
# 1)Short strings and long strings- using""" fot longer one

# 2)Function len- length of a variable .   len(variable)

# 3)IF statement - if True:, or if False: 
#                       print("something") - do not forget to make space 

# 4)printing a length of a long string- do not miss a "space" while counting  letters 

# 5)Positions(Indexes) of  letters in string-  full_name[0]-the first letter

# 6)printing letters from string- print("letter"in string) or print("letter"not in string)
#                        The result is True-if there is the letter you want, False-if there is not the letter you are looking for.

# 7)Slicing strings-  print(full_name[2:9])- starting  with 2 and ending  with 8 -RULE
#   Print(full_name[:5])=[from 0 to 4] print(full_name[2:])=[from 2 to the last letter]

# 8)guideline of skiiping letters- print(full_name[2:9:2]) START-FINISH-STEP

# 9)printing the negative index- print(full_name[-1])-printing the last letter

#10)string.upper - encreasing the letters
#11)string.lower-decreasing the letters
#12)STRIP-cutting the space
#13)replace-replacing the variable to another variable.
#----------------------------
#GROUP 4

print(7+10)
print(10-5)
print(10*4)
print(10/2)
print(10//2)
print(5//4)
print(20%2)
print(40%6) #4


price=80
price=100
print(price) #

#classwork

mum_age=50
print(mum_age)
dad_age=55
print(dad_age)
Nika_age=16
print(Nika_age)
Demetre_age=12
print(Demetre_age)
grandma_age=78
print(grandma_age)
grandpa_age=82
print(grandpa_age)

#after 5 years
string1="----------------------"
print(string1)
mum_age=55
print(mum_age)
dad_age=60
print(dad_age)
Nika_age=21
print(Nika_age)
Demetre_age=17
print(Demetre_age)
grandma_age=83
print(grandma_age)
grandpa_age=87
print(grandpa_age)

#Also you can write  like that: mum_age+=5 
