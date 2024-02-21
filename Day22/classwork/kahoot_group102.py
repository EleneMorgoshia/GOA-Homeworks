#1)yellow  - 
#2)error +
#3) error -
#4)red +
#5)blue +
#6)blue +
#7)yellow -
#8)yellow - (what??) დაუნდობელი იყო...
#9)red +
#10) yellow +
#11)blue +
#12)blue -

#1)
def lashas_mama(num):
    return str(num)

print(lashas_mama(80085)) #ტერმინალში როცა ვპრინტავთ სტრინგს, ბრჭყალები ეშლება :) 

#3)
def nacarqeqia(str_1,str_2):
    return str_1[0] == str_2[0] and str_1[-1] == str_2[-1]

print(nacarqeqia(input('aa'),input('e')))  # დააბრუნებს false 
#input 1 - iyo arabets rostevan
#inpu 2 - iyo erti komble

# name = input('ee')
# print(name)

#7)
def shuala(s):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    if len(s) % 2 == 0:
        return s[len(s)//2 -1] + s[len(s) // 2]
    
titi = 'hello my brothers and sister ანუ ძმანო და დანო ტანო ტატანო'
print(shuala(titi))


titi = 'hello my brothers and sister ანუ ძმანო და დანო ტანო ტატანო'
print(len(titi)) #აბოსულუტურად ყველა  ასოს თვლის 
