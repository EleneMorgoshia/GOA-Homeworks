# def zipped(aa,bb,cc):
#     x = list(zip(aa,bb,cc))
#     print(x)
#     x = "".join("".join(char) for char in zip (aa,bb,cc))
#     print(x)

# zipped(["a","b","c","d"],["1","2","3","4"],["sandro","misha","dato","nika"])
#ჯოინ ფუნქციის გარეშე დაწერეთ იგივე ფუნქცია
#უნდა გამოვიდეს a1sandrob2mishac3datod4nika
def zipped(first_arr , second_arr , third_arr):
    result_arr = []
    for i in range(len(first_arr)):
        for k in range(len(second_arr)):
            result_arr.append(first_arr[i])
            result_arr.append(second_arr[i])
            result_str = ""
    return result_arr
    

print(zipped(["a","b","c","d"],["1","2","3","4"],["sandro","misha","dato","nika"]))
#ამოხნსა Day19-ის classwork_group102-ის ფაილში 