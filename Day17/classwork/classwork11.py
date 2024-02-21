#task 7:
#Given a string of digits, you should replace 
#any digit below 5 with '0' and any digit 5 and 
#above with '1'. Return the resulting string.
#Note: input will never be an empty string
#["01011110001100111", "45385593107843568"]
def fake_bin(x):
    new_str = ''
    for i in range(len(x)):
        if int(x[i]) < 5:
            variable_for_adding_zero_in_new_str = '0'
            new_str += variable_for_adding_zero_in_new_str
        elif int(x[i]) >= 5:
            variable_for_adding_one_in_new_str = '1'
            new_str += variable_for_adding_one_in_new_str
    return new_str

print(fake_bin("45385593107843568"))

#better version
def fake_bin(x):
    final_str = ''
    for char in x:
        if int(char) < 5:
            final_str += '0'
        elif int(char) >= 5:
            final_str += '1'
    return final_str

print(fake_bin("45385593107843568"))