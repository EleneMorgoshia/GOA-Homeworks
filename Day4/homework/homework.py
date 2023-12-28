#group4: quise3
#group 102: #homework:ask user to enter 2 names and  print the name that will have more consonant.use format method for beautiful sentence.
first_name=input("enter first name pls: ")
second_name=input("enter second name pls: ")
#incrementation variable
amount_of_consonants_in_first_name=0
amount_of_consonants_in_second_name=0

#how to find out which names has more consonants
for char in first_name:
    if char not in "aeiou":
        amount_of_consonants_in_first_name+=1

for char in second_name:
    if char not in "aeiou":
        amount_of_consonants_in_second_name+=1

if amount_of_consonants_in_first_name>amount_of_consonants_in_second_name:
    print("The first name has more consonants and it contains {} consonants".format(amount_of_consonants_in_first_name))
elif amount_of_consonants_in_second_name>amount_of_consonants_in_first_name:
    print("The second name has more consonants and it containts {} consonants".format(amount_of_consonants_in_second_name))
else:
    print("Both names have same consonants!")