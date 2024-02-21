#შექმენით ფუნქცია ,რომელიც მოხმარებელს შემოატანინებს
#ტექსტს და უნდა დაწეროთ ალგორითმი,რომელიც დააბრუნებს
#მოხმარებლის მიერ შემოყვანილ ტექსტს , ოღონდ t ასოებს გადიდებულს.
#for ციკლის გარეშე

def find_t(str_name):
    result_str = ''
    for char in str_name:
        if char == 't':
           result_str =  str_name.replace('t','T')
    return result_str

str_variable = input('Enter some text here:')
print(find_t(str_variable))

#without for 
def encrease_t(str_name):
    result_str = str_name.replace('t','T')
    return result_str


str_variable = input('Enter some text here:')
print(encrease_t(str_variable))