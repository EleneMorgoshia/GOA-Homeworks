#group4:
#working on homeworks
#1)write a function that accepts  an integer n and a string s
#as parameters and returns a string of s repeted exactly n times

def repeat_str(repeat,string):
    new_str = ""
    for i in range(repeat):
        new_str += string
    return new_str

print(repeat_str(3,"GOA"))

#2)it's preatty straightforward.your youal is to create a function that
# removes the first and last characters of a string.you're giveen one parameter,
#the original string.you don't have to worry wit hstring with less than two characters
# def remove_char(s):
#     return s[1:-1]


#with using loops *
def remove_char(s):
    result = ""
    my_arr=[]
    for i in range(len(s)):
        if i != 0 and i != len(s)-1:
            my_arr.append(i)
            print(my_arr)
    for j in my_arr:
        print(s[j])
        result += s[j]
    return result

print(remove_char("elene"))

# print(remove_char("elene"))
#3)find the smallest integer in the array
arr=[1,2,100,80.70,90]
print(min(arr)) #აბრუნებბს ლისთში მინიმუმს
print(max(arr)) #აბრუნებს ლისთში მაქსიმუმს