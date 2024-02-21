#split and join methods

#split - ლისთად გადააქცევს სტრინგს
x = 'Elene Morgoshia'
print(x.split()) 

#join - ლისთში არსებულ ელემენტებს ერთმანეთს მიაწეპებს და სტრინგად  გვექნება შედეგი 
y = ['Elene','Erekle','Ioane']
result = "".join(y)
print(result)

def reverse_words(s):
    split_arr = s.split(" ")
    split_arr.reverse()
    result = ""
    for element in split_arr:
        result += element + " "
    return result[:-1]


print(reverse_words("I want ice cream"))