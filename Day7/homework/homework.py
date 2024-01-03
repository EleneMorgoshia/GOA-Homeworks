#group4: quise 5]
#1)შექმენით სია, სადაც გადასცემთ რამის ლიდერების სახელს და გვარს
#ელემენტებად. გამოიტანეთ თქვენი რაზმის ლიდერის სახელი

#2)შექმენით თქვენი რაზმის წევრებისგან სია
#დაპრინტეთ შუა 5 რაზმის წევრი

#3)შექმენით სია,სადაც იქნება რამდნეიმე ხილის სახელი და 1 ბოსტნეული
#თქვენ უნდა შეცვალოთ ეს ბოსტნეული სხვა რაიმე ხილით და დაპრინტოთ სია


# homework1:
group_leaders_names=["Dato Tyeshelashvili","Nikoloz Filishvili","Gabriel Molodini","Dato janezashvili"]
name_of_my_leader=group_leaders_names[0]
print("My leader's name is: {}".format(name_of_my_leader))

#homework2
group_members=["Elene morgoshia","Lizi Rusadze","Tamuna Gelenava","Sali Saltauras","Nikoloz Morgoshia","Demetre Morgoshia","Erekle Kapanadze"]
print(group_members[1:5])

#homework3
fruits_plus_one_vegetable=["banana","apple","orange","potato","cucumber","grapes"]
fruits_plus_one_vegetable[4]="Pear"  #on the left should write the value of the list (the one you want to change) and on the right, you should write new(changed) value
print(fruits_plus_one_vegetable)

#-------------------------------
#group 102: 

#homeworkN1:1)scores=[20,43,56,73,10,6,87,45,97] სორტის გამოყენების გარეშე დააბრუნეთ ყველაზე დიდი რიცხვი.
scores = [20, 43, 56, 73, 10, 6, 87, 45, 97]
max = scores[0]
i = 0
while i < len(scores):
    if scores[i] > max:
        max = scores[i]
    i += 1
print(max)

#2)homeworkN2: students=["nika","ana","mamuka","iva","farna"] შეატრიალეთ უკუღმა sort  და reverse მეთოდის გარეშე.
#მინიშნება: while ციკლით სათითად შეამოწმეთ ელემენტი და 
#მის მარჯვნივ მდგომი,რომელიც უფრო დიდი იქნება,დროებით მიანიჭეთ მაქსიმუმის მნიშვნელობა და 
#შემდეგ შეადარეთ მის მარვნის მდგომს

students=["nika","ana","mamuka","iva","farna"]
#farna,iva,mamuka,ana,nika
new_students=[]
new_students.append(students[-1])
new_students.append(students[-2])
new_students.append(students[-3])
new_students.append(students[-4])
new_students.append(students[-5])
print(new_students)