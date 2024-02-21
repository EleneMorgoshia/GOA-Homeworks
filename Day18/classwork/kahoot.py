#kahoot
# 1)error-
# 2)len(greeting)+
# 3)out of range error+
# 4)...........-
# 5)arcerti -
# 6)error-
# 6)araferi-
# 8)arcerti-
# 9)99 imitoro gori araa +
#ძნ დაუნდობელი იყოოოო

#----------------------
# function abs
list_num =list(range(abs(-3),7) ) #range (3,7) anu [3,4,5,6]
print(list_num)
#-----------
b = list(range(1,6,2)) #1,3,5 (1იდან 6 ამდე 2 ნახტომით)
print(b)
c = range(1,10,2)
print(list(c))

a = [4,1,2,3]
b = list(range(1,6,2))  #b= [1,3,5]
for i in a:
    b.append(a[5]+a[i]) #a[5] - a სიას ინდექს 5 ზე მდგარი ელემენტი საერთოდ არ აქვს

print(b)
#------------------
list = [[3,5],
         [2,1,4,1],
         [1,1,2]]
print(list[list[2][list[1][3]]][2])
print(list[list[2][list[1][3]]][2])
#--------------------------
full_name = 'jeki-chadi'
for char in full_name[ 5::2]: #მეხუთედან სტრინგის ბოლომდე  ყოველი მეორე 
    if char == 'c':
        break
    print(char)
#----------------------------
numbers = list(range(50,10,-5)) #50-იდან 10-ამდე ყოველი მეხუთე (50,45,40,30...)
for number in numbers:
    if number <= 0:
        break 
    print(number -20)