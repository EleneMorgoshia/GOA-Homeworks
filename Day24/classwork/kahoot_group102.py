#1)blue -  red
#2)green +
#3)yellow ---- :(((
#4)error - 
#5)არ ვიცით ჯერ
#6) არ ვიცით ჯერ
#7)error -
#8)red +
#9)green - 
#10) არ ვიცით ჯერ
#11) 4 -
#12)yellow
#N.O C.O.M.M.E.N.T

#-------------
#1)
my_str = 'G@e @lagnoL @idz@e '
print(my_str.count(' @')) #count ითვლის რაოდენობას იმ პარამეტრისას, რასაც გადავცემთ

#2)

def split(p):
    if len(p) % 2 == 0:
        p = p.replace(p[len(p) // 2], "==" + p[len(p) // 2])
    else: #ამ შემთხვევაში else-ში გადმოხტება , რადგან 11 % 2 == 1 
        p = p.replace(p[len(p)// 2], '-' + p[len(p)//2] + '-')
        #p[len(p) // 2] - 'j' ჩანაცვლდება   , '-' + p[len(p) // 2] + '-' = -j-  თი
    return p

user_input = input("გილოცავთ ნიკოლოზობას") #input = ელ_Gujinhhoo
print(split('ელ_Gujinhho'))

#3)

def amognsus(my_str):
    my_str = my_str.replace("'",'ღ')
    # print(my_str)
    my_str = my_str.title() # თითოეული სიტყვის პირველ ასოს გაადიდებს (ჩვენ სტრინგში \-ის მერე რაც წერია მაგასაც გაადიდებს  )
    # print(my_str)
    my_str = my_str.replace("ღ","'")
    print(my_str)

user_str = "ge'las wy'u\"rya wy'ali" #\ საშუალებას გვაძლევს ,რომ სტრინგში ორი ბრჭყალი გამოვიყენოთ(""") ისე ,რომ არ დააეროროს
amognsus(user_str)

#4) რას დააბრუნებს ფუნქცია და არა 'რას დაპრინტავს' 
def shilaki(str):
    str = str.lower()
    new_str = ''
    for char in str:
        if str.count(char) == 1:
            new_Str += '('
        else:
            new_str += ')'
        return new_str

user_str = input('2e135')  # input = XGjKyJV
print(shilaki(user_str) + 64120 ) #ეს რეალურად ერორს დაარტყამდა

#7)
my_list = ['nika','gio','dato','luka','lashasmama','lasha','tamarmefe','mari']
def remove_all(my_list):
    arr = []
    x = 10 + 10 - 40 + 20  # x = 0 
    y = len(my_list) - 34 + 16 +14 - 38 + 4 - 8 + 2 + 1 + 1 + 17 * 2 * 1 # y = len(my_list)
    z = 2 * 2  - 2 - 1 - 1 # z = 0
    for i in range( x,y,z):
        arr.append(my_list[i])
    
    return arr

print(remove_all(my_list))

#9)
sum = 1
counter = 0
for i in range(5):
    x = 0
    if x < 1 :
        sum += i
        counter += i
        x += 1
    else:
        break


print(counter + sum) # 10 + 11 = 21 

#11)

i = 20 
while i >= 0:
    print(i) # 20 , 15 
    i -= 5
    if i == 0:# აქამდე რომ მოვიდოდა , მერე დაერორდებოდა
        raise 'geal'
    i += 2.5

#უმაგრესი kahoot იყო...
