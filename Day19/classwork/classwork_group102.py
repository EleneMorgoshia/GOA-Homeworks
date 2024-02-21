#working on homework
def zipped(first_arr , second_arr , third_arr):
    my_arr = []
    result_str = ""
    i = 0
    while i < len(first_arr):
        result_str += first_arr[i]
        result_str += str(second_arr[i])
        result_str += third_arr[i]
        i += 1
        my_arr.append(result_str) #ლისთის ელემენტებად რომ ჩავწეროთ
        result_str = ""
    return  my_arr


print(zipped(["a","b","c","d"],[1,2,3,4],["sandro","misha","dato","nika"]))

# დაწერეთ იგივე ამოცანა, პლუს პირობა არის ის რომ ლისთებში სხვადასხვა რაოდენობის ელემენტებია
def zipped(first_arr , second_arr , third_arr):
    result_str =""
    i = 0
    min_len = min(len(first_arr), len(second_arr), len(third_arr))
    while i < min_len:
        result_str += first_arr[i]
        result_str += str(second_arr[i])
        result_str += third_arr[i]   
        i += 1
    return result_str

print(zipped(["a","b","c","d"],[1,2,3],["sandro","misha","dato","nika"]))
 
#-----------------------
# min function
my_list = [10,20,30]
print(min(my_list)) #ითვლის მინიმალურს სიაში

